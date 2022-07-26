### Date created
GitHub project created on July 25, 2022
The README file was originally created in the GitHub repository
from which it was forked, but then updated on July 25, 2022.

### Project Title
BikeShare_2

### Description
Describe what your project is about and what it does
Bikeshare_2 is a python program that will show some data from the bikeshare data for analysis.  The data is stored in a CSV file that matches the city's name.

When running this program, when prompted, answer with a string that is the city name, the month or ALL for all the months, and the day or ALL for all the days.
For the city, type one of the following, followed by a comma:
* Chicago
* New York City
* Washington

For the month, type ALL or the month number (1-6) or the month name (January through June) or the 3-letter month abbreviation (Jan thru Jun), followed by a comma.

For the day, type ALL or the day number (1-7 with 1 being Sunday), the month name (e.g. Sunday), or the three letter abbreviation for the day.

The program will display the following information:
* What is the most common month
* What is the most common day of the week
* What is the most common start hour
* What is the most common start station
* What is the most common destination station
* What is the most common combination of start and destination station
* What is the total travel time
* What is the mean travel time
* What are the number of user types per user type (e.g. subscriber)
* Where available, what is the breakdown of users' genders
* Where available, what is the earliest, latest, and most common birth year
* What are the number of trips per month, sorted a couple of different ways
* What are the number of trips per day of week, sorted by most popular day to least
* What are the number of trips per start hour, sorted by most popular start hour to least
* What stations were both the start and destination stations for the same trips and how often
* What are the start stations, sorted by most popular to least
* What are the end stations, sorted by most popular to least
* Summary statistics about the trip durations
* What were the mean trip durations by month and by day of week
* What were the user types totals by month and by day of week


### Files used
Python file:
* bikeshare_2.py

CSV files (but not included in this project):
* chicago.csv
* new_york_city.csv
* washington.csv


### Credits
References:
* https://peps.python.org/pep-0257/ -- Docstring conventions
* https://peps.python.org/pep-0498/ -- Look at string interpolation
* https://www.w3schools.com/python/ -- use to check python syntax
* https://stackoverflow.com/questions/30222533/create-a-day-of-week-column-in-a-pandas-dataframe-using-python
* https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas
* https://datascientyst.com/convert-month-number-to-month-name-pandas-dataframe/
* https://www.geeksforgeeks.org/python-output-formatting/
* https://pandas.pydata.org/docs/reference/api/pandas.Series.iteritems.html
* https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html
* https://www.w3schools.com/python/ref_string_split.asp
* https://www.w3schools.com/python/gloss_python_array_length.asp
* https://stackoverflow.com/questions/761804/how-do-i-trim-whitespace-from-a-string
* PyCharm as an IDE which helped with the input into string variables
* Book: Python for Data Analysis 2nd Edition by Wes McKinney

Some changes in the file were based on feedback provided by Udacity reviewers.
