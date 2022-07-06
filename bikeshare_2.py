import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

#Function to get filters through user input

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print()
    print('Hello! Let\'s explore some US bikeshare data!')


    # Get user input for CITY (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
    city = input('Which city would you like to analyze: Chicago, New York City or Washington? ').title()
    cities = ['Chicago', 'New York City', 'Washington']

    while city not in cities:
        print()
        print('Please check your spelling and try again!')
        city = input('Which city would you like to analyze: Chicago, New York City or Washington? ').title()


    # Get user input for MONTH (all, january, february, ... , june)
    print()
    print('Okay, let us take a look at the data for {}.'.format(city))
    month = input('Which month would you like to analyze: All, January, February, March, April, May or June? ').title()
    months = ['All','January', 'February', 'March', 'April', 'May', 'June']


    while month not in months:
        print()
        print('Please check your spelling and try again! Options: All, January, February, March, April, May or June.')
        month = input('Which month would you like to analyze? ').title()


    # Get user input for DAY of week (all, monday, tuesday, ... sunday)
    if month != "All":
        print()
        print('Okay, let us take a look at the data for {} for {}.'.format(month,city))


    else:
        print()
        print('Okay, let us take a look at the data for all months for {}.'.format(city))

    day = input('Which day of the week would you like to analyze: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? ').title()
    days = ['All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']


    while day not in days:
        print()
        print('Please check your spelling and try again! Options: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.')
        day = input('Which day of the week would you like to analyze? ').title()

    if day != "All" and month != "All":
        print()
        print('Okay, let us take a look at the data for {}s in {} for {}.'.format(day,month,city))
    elif day == "All" and month != "All":
        print()
        print('Okay, let us take a look at the data for all days of the week for {} for {}.'.format(month,city))
    elif day != "All" and month == "All":
        print()
        print('Okay, let us take a look at the data for {}s for all months for {}.'.format(day,city))
    elif day == "All" and month == "All":
        print()
        print('Okay, let us take a look at the data for all days of the week for all months for {}.'.format(city))


    print()
    print('-'*40)
    return city, month, day

#Function to load data according to the selected filters

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extract month and day from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday


    # Filter by month (if applicable)
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)
        df = df[df['month'] == month]

    # Filter by day of week (if applicable)
    if day != 'All':
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = days.index(day)
        df = df[df['day'] == day]

    if city == 'Washington':
        df['Gender'] = "No data."
        df['Birth Year'] = "No data."
    return df


#Function to get the time statistics

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print("Most popular month: ", popular_month + 1, " (e.g. January = 1)")

    # Display the most common day of week
    popular_day = df['day'].mode()[0]
    print("Most popular day: ", popular_day + 1, " (e.g. Monday = 1)")

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most popular hour: ", popular_hour + 1, " (e.g. 0 = 12 a.m.)")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most popular start station: ", popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most popular end station: ", popular_end_station)

    # Display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + " to " + df['End Station']
    print("Most frequent combination: {}".format(df['Start to End'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    df['hour start'] = df['Start Time'].dt.hour
    df['hour end'] = df['End Time'].dt.hour


    total_travel_time = (df['hour end'] - df['hour start']).sum(skipna=True)
    print("Total travel time: ", total_travel_time, "hours.")

    # Display mean travel time
    mean_travel_time = (df['hour end'] - df['hour start']).mean(skipna=True)
    print("Mean travel time: ", mean_travel_time, "hours.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print(user_types)
    print()


    # Display counts of gender
    gender = df['Gender'].value_counts().to_frame()
    print(gender)
    print()


    # Display earliest, most recent, and most common year of birth
    earliest_dob = df['Birth Year'].min()
    print("Earliest year of birth:", earliest_dob)
    print()

    most_recent_dob = df['Birth Year'].max()
    print("Most recent year of birth:", most_recent_dob)
    print()

    most_common_dob = df['Birth Year'].mode()[0]
    print("Most common year of birth:", most_common_dob)
    print()




    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)

    # Continously ask user if he wishes to see raw data
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter Yes or No: ').title()
    start_loc = 0

    while view_data == "Yes":
        print(df.iloc[0 + start_loc:5 + start_loc])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").title()




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter Yes or No: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
