import time
import pandas as pd

# Value to use to indicate "all" for either the month or day of the week.
# The other numbers will be used directly.
ALL = 0

# Use a constant to indicate that a matching key was not found
NOT_FOUND = -1

# The tuple indices for the display value and all the allowed values
NAME_IDX = 0
INPUT_VALUES_IDX = 1

# The city names and their CSV files
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# Allowed entries for the month -- all, month name, abbreviation, or month number
# The structure is the numeric value to use followed by its label and all its allowed input values
ALLOWED_MONTH_SELECTION = {ALL: ('All', {'all'}),
                           1: ('January', {'january', 'jan', '1', '01'}),
                           2: ('February', {'february', 'feb', '2', '02'}),
                           3: ('March', {'march', 'mar', '3', '03'}),
                           4: ('April', {'april', 'apr', '4', '04'}),
                           5: ('May', {'may', '5', '05'}),
                           6: ('June', {'june', 'jun', '6', '06'})}

# Allowed entries for the day of the week -- all, day name, abbreviation, one/two character abbreviation, or number
# The structure is the numeric value to use followed by all its allowed input values
ALLOWED_DAY_SELECTION = {ALL: ('All', {'all'}),
                         1: ('Sunday', {'sunday', 'sun', '1'}),
                         2: ('Monday', {'monday', 'mon', '2'}),
                         3: ('Tuesday', {'tuesday', 'tue', '3'}),
                         4: ('Wednesday', {'wednesday', 'wed', '4'}),
                         5: ('Thursday', {'thursday', 'thu', '5'}),
                         6: ('Friday', {'friday', 'fri', '6'}),
                         7: ('Saturday', {'saturday', 'sat', '7'})}

# Dictionary for yes/no questions
YES_NO_SELECTION = {'Yes': ('yes', {'y', 'yes'}),
                    'No': ('no', {'n', 'no'})}


def get_answer_for_prompt(prompt):
    """
    Given a prompt to be displayed, return a string for the user's response

    Args:
        (str) prompt: Prompt to be displayed

    Returns:
        The input from the user
    """
    try:
        input_str: str = input(prompt)
    except Exception as error:
        print(error)
        input_str = ''

    return input_str


def get_key_for_value(input_value, allowed_inputs):
    """
    Given an input value and a dictionary of allowed values, return the key that matches the input value

    Args:
        (str) input_value: value from the user
        (dict) allowed_inputs: a dictionary of keys and the allowed values that map to those keys

    Returns:
        The key from the dictionary that matches the input value, or NOT_FOUND if nothing was found
    """
    # initialize the value to be returned
    matched_key = NOT_FOUND

    # Loop through each key in the dictionary and see if the input string is one of the allowed strings
    for key in allowed_inputs:
        if input_value.lower() in (allowed_inputs[key][INPUT_VALUES_IDX]):
            matched_key = key
            break

    return matched_key


def get_user_input(prompt, error_msg, allowed_values, includeExtraLine=True):
    """
    Asks the user the prompt and then verifies that the value, converted to lower case,
    is one of the allowed values.

    Args:
        (str) prompt: The prompt to show to the user.
        (str) error_msg: The error message to display if the input value is not in allowed values
        (dict) allowed_values: A dictionary of allowed values
        (bool) includeExtraLine: Boolean indicating if a newline should be added

    Returns:
        (int) return_value - the value of the key that matches the input value
    """
    # Initialize the return_value which will be checked
    return_value = NOT_FOUND

    # Add a blank line to start if needed
    if includeExtraLine:
        print('\n')

    # While the return value is NOT_FOUND, prompt the user for an input value, get its
    # matching key, and if it is not found display the error
    while return_value == NOT_FOUND:
        input_value = get_answer_for_prompt(prompt)
        return_value = get_key_for_value(input_value, allowed_values)
        if return_value == NOT_FOUND:
            print(error_msg)

    # return the value that matches the input from the user
    return return_value


def ask_should_show_more_data():
    """
    Asks the user if the program should show more data and allow for y/n or yes/no responses

    Returns:
        (bool) return_value - whether to continue showing data
    """
    # While the return value is NOT_FOUND, prompt the user if the program should show more data and
    # continue asking until there is a y, yes, n, no
    returned_answer = get_user_input('Do you want to see more of this data? (y/n or yes/no)',
                                     'Please enter "y" or "yes" or "n" or "no"',
                                     YES_NO_SELECTION,
                                     False)

    # return the value that matches the input from the user
    return returned_answer == "Yes"


def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - the number of the month in the year, or 0 for all
        (int) day - the number of the day in the week, or 0 for all
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Set up variables with initial values to be used to determine what the user requested
    city = ''
    month = NOT_FOUND
    day = NOT_FOUND
    request_info = True

    # Set up the prompt for the user
    prompt = 'Please enter a city (Chicago, New York City, or Washington), the month (January through June or ALL), ' \
             'and the day of the week (or All) (using commas to separate the values: '

    # While we should request the information for the analysis, prompt the user for the input and
    # determine which city, month, and day we should use, or show an error and ask the user again.
    while request_info:
        try:
            input_str: str = input(prompt)
            # Split the input string on commas to separate out the city, month, and day
            input_values = input_str.split(',')

            # Reset the variables for the values that will be returned.  If any of these are
            # in error, that will determine the additional error messages.
            city = ''
            month = NOT_FOUND
            day = NOT_FOUND

            # If the number of input values match, then try to match the first value
            # to a city, the second value to a month (or ALL), and the third value
            # to a day (or ALL)
            if len(input_values) == 3:
                if input_values[0].strip().lower() in CITY_DATA:
                    city = input_values[0].strip()

                # See if the month and the day are allowed values
                month = get_key_for_value(input_values[1].strip().lower(), ALLOWED_MONTH_SELECTION)
                day = get_key_for_value(input_values[2].strip().lower(), ALLOWED_DAY_SELECTION)
                if city == '':
                    print('Please enter a city from the list: Chicago, New York City, Washington')
                if month == NOT_FOUND:
                    print('Please enter a month from January to June (or use a three letter abbreviation or the month '
                          'number) or specify ALL.')
                if day == NOT_FOUND:
                    print('Please enter a day of the week (or use a three letter abbreviation or the day number) or '
                          'specify ALL.')

                # If the city and the month and day are specified, then there is no need to continue prompting the user
                request_info = city == '' or month == NOT_FOUND or day == NOT_FOUND

            else:
                # We did not get three parameters
                print('Please specify the city, the month (or all), and the day (or all) with commas between them.')
        except Exception as error:
            print(error)

    # Return the selection values
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - key to the month to filter by, or ALL to apply no month filter
        (int) day - the day of week to filter by, or ALL to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])

    # Convert the start and end times to date time types
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Add the month and the day of week columns to the data frame because they could be used in filtering
    # and displaying.  Added the month number to help in sorting.
    df['month'] = df['Start Time'].dt.month_name()
    df['month_no'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    # Filter by the month if selected
    if month != ALL:
        df = df[df['month'] == ALLOWED_MONTH_SELECTION[month][NAME_IDX]]

    # Filter by the day of the week if selected
    if day != ALL:
        df = df[df['day_of_week'] == ALLOWED_DAY_SELECTION[day][NAME_IDX]]

    return df


def display_most_common_value(df, field_name, display_name):
    """
    Displays statistics on the most frequent values

    Args:
        (Pandas DataFrame) df: data frame of bike share data
        (str) field_name: field name to use in analysis
        (str) display_name: name to include in output
    """
    val = df[field_name].mode()[0]
    print(f'The most common {display_name} is {val}')


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    display_most_common_value(df, 'month', 'month')

    # display the most common day of week
    display_most_common_value(df, 'day_of_week', 'day of the week')

    # display the most common start hour
    display_most_common_value(df, 'start_hour', 'start hour')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    display_most_common_value(df, 'Start Station', 'start station')

    # display most commonly used end station
    display_most_common_value(df, 'End Station', 'end station')

    # display most frequent combination of start station and end station trip
    df['start_end_dest'] = 'Start: ' + df['Start Station'] + '  End: ' + df['End Station']
    display_most_common_value(df, 'start_end_dest', 'start and end station pair')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'The total travel time is {total_travel_time}')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'The mean travel time is {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('User types:')
    print(user_types_counts)
    print()

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Genders:')
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
        print()

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        max_birth_year = df['Birth Year'].max()
        min_birth_year = df['Birth Year'].min()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Birth Years:')
        print(f'Earliest = {min_birth_year}')
        print(f'Latest = {max_birth_year}')
        print(f'Most Common = {most_common_birth_year}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def additional_time_stats(df):
    """
    Displays additional information about the bikeshare trips -- like the number of trips
    per month, etc.

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nShow additional day and month information...\n')

    # Display the number of trips per month
    print('Number of trips per month ordered by number of trips descending:')
    num_trips_per_month = df['month'].value_counts()
    print(num_trips_per_month)

    # Display the number of trips per month
    print('\nNumber of trips per month ordered by month:')
    num_trips_per_month = df[['month_no', 'month']].value_counts().sort_index()
    print(num_trips_per_month)

    # Display the number of trips per day of week
    print('\nNumber of trips per day of week sorted by number of trips descending:')
    num_trips_per_day_of_week = df['day_of_week'].value_counts()
    print(num_trips_per_day_of_week)

    # Show the number of trips per start hour
    print('\nNumber of trips per start hour by number of trips descending:')
    num_trips_per_start_hour = df['start_hour'].value_counts()
    print(' Hour  Trips')
    num_printed = 0
    for index, row in num_trips_per_start_hour.iteritems():
        # Moved the prompt before printing the next line in case the number of hours is a multiple of 5 --
        # did not want to prompt the user and then show nothing
        if num_printed % 5 == 0 and num_printed > 0:
            show_more = ask_should_show_more_data()
            if not show_more:
                break
        print('%5d   %7d' % (index, row))
        num_printed += 1

    print('-' * 40)


def show_sequence_data(original_seq, rows_at_a_time=5):
    """
    Displays the sequence of data 5 rows at a time and asks the user if the program should show more.

    Args:
        (Pandas Sequence) original_seq: sequence of data for display
        (int) Number of rows to display at a time, default to 5
    """
    start_index = 0
    end_index = rows_at_a_time if original_seq.size >= rows_at_a_time else original_seq.size
    while start_index < original_seq.size:
        seq = original_seq.iloc[start_index:end_index]
        print(seq)
        if end_index < original_seq.size:
            if not ask_should_show_more_data():
                break
        start_index += rows_at_a_time
        end_index += rows_at_a_time
        if end_index > original_seq.size:
            end_index = original_seq.size


def additional_station_stats(df):
    """
    Displays additional information about the stations, including how many trips there were where
    the start and end stations are the same.

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nShow additional information about the stations...\n')

    # Display the number of times the start and end stations are the same
    print('Trips where the start and end stations were the same (i.e. round trips):')
    same_dest = df[df['Start Station'] == df['End Station']]
    same_dest_values = same_dest['Start Station'].value_counts()
    print(same_dest_values)

    # Display the statistics about when the start and end destinations are the same -- the most and least
    # numbers, the mean, etc.
    print('\nSummary statistics for when the start and end destinations are the same:')
    print(same_dest_values.describe())

    # Display the most popular start stations, 5 at a time, this time using a sequence as opposed
    # to iteritems function
    print('\nThe most popular start stations:')
    start_stations = df['Start Station'].value_counts()
    show_sequence_data(start_stations)

    # Display the most popular end stations, 5 at a time, this time using a sequence
    print('\nThe most popular end stations:')
    end_stations = df['End Station'].value_counts()
    show_sequence_data(end_stations)

    print('-' * 40)


def additional_trip_duration_stats(df):
    """
    Displays additional trip duration statistics using describe but also shows the average
    per month and the average per day of the week

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nShow the trip duration summary statistics...\n')
    start_time = time.time()

    # Show the min, max, mean, etc. of the trip duration values
    print('\nSummary statistics for the trip duration:')
    print(df['Trip Duration'].describe())

    # Show the mean trip duration by month
    print('\nMean trip duration per month:')
    print(df.groupby(['month_no'])['Trip Duration'].mean())

    # Show the mean trip duration by day of week
    print('\nMean trip duration per day of week:')
    print(df.groupby(['day_of_week'])['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def additional_user_stats(df):
    """
    Displays additional user statistics to see if the number of customers seems to sharply
    increase during the weekends or as the weather warms and more tourists arrive.

    Args:
        (Pandas DataFrame) df: data frame of bike share data
    """
    print('\nShowing additional User Stats...\n')

    # Show the user types by month.  Should we see more customers (as opposed to subscribers)
    # as we approach the months linked with tourism?
    print('The user types and counts by month:')
    print(df.groupby(['month_no'])['User Type'].value_counts())

    # Show the user types by the day of the week to see if we have more customers on the weekends --
    # tourists and other visitors possibly.
    print('\nThe user types and counts by day of week using the day name:')
    print(df.groupby(['day_of_week'])['User Type'].value_counts())

    print('-' * 40)


def main():
    """ Repeatedly ask the user for the city, month, and day, and display information from the CSV file. """
    while True:
        city, month, day = get_filters()
        print(f'You selected the city = {city}, the month {ALLOWED_MONTH_SELECTION[month][NAME_IDX]}, '
              f'and the day {ALLOWED_DAY_SELECTION[day][NAME_IDX]}')
        df = load_data(city, month, day)

        # Run the functions with the questions initially asked
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Run the functions that include additional information
        additional_time_stats(df)
        additional_station_stats(df)
        additional_trip_duration_stats(df)
        additional_user_stats(df)

        try:
            restart: str = input(
                '\nWould you like to restart? Enter yes or no. (Anything other than yes will be considered no.) \n')
        except Exception as error:
            print(error)
            restart = 'no'

        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
