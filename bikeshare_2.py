import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('A project made by AI')
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('~~~~~~~~~~~~~~~~~~~~')
    print()
    c = ['chicago', 'new york city', 'washington']
    while True:
        print()
        city= input('Enter city name[chicago, new york city, washington]:').lower()
        if city in c:
            break
        print('Invalid City')
       
    # get user input for month (all, january, february, ... , june)
    m = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        print()
        month= input('Enter Month[all, january, february, march, april, may, june]:')
        if month in m:
            break 
        print ('Invalid Month')
        print('--------------------')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    d= ['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']
    while True:
        print()
        day= input('Enter Day of the week[all, monday, tuesday,wednesday, thursday, friday, saturday, sunday]: ').lower()
        if day in d:
            break
        print('Invalid Day')

    print('-'*40)
    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print()

    # display the most common month
    print('Most Common Month:', df['month'].mode()[0])


    # display the most common day of week
    print('Most Common Day:', df['day_of_week'].mode()[0])


    # display the most common start hour
    print('Most Common Hour:', df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('-------------------------------------------------------')

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print()

    # display most commonly used start station
    print('Most Commonly used Start Station:', df['Start Station'].mode()[0])


    # display most commonly used end station
    print('Most Commonly used End Station:', df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    print('Comibation of most frequent start and end station:', df.groupby(['Start Station', 'End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('-'*40)
    print('-'*40)

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time:',total_time )


    # display mean travel time
    print('Mean Travel Time:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('-'*40)
    print('-'*40)

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(' ')

    # Display counts of user types
    print('Counts of User Types:', df['User Type'].value_counts())
    print()
    print()


    # Display counts of gender
    try: 
        gender_type = df['Gender'].value_counts()
        print('Counts of Gender:', gender_type)
    except KeyError:
        print('No data available for Gender Types for your selected month.')
    print()


    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year =  df['Birth Year'].min()
        print('Earliest Birth Year', earliest_year)
    except KeyError:
        print('No data available for Earliest Birth Year for your selected month.')
    
    print()

    try:
        recent_year = df['Birth Year'].max()
        print('Most Recent Birth Year', recent_year)
    except KeyError:
        print('No data available for Most Recent Birth Year for your selected month.')
    print()

    try: 
        common_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year', common_year)
    except KeyError:
        print('No data available for Common Birth Year for your selected month')

    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)

def raw_data_user(df):
    #print raw data on demand of user 
    st = 0 
    raw_data = input('\n Would you like to see raw data? Enter yes or no.\n')
    while raw_data.lower() == 'yes':
        df_slice = df.iloc[st: st+5]
        print(df_slice)
        st += 5 
        raw_data = input('\n Would you like to see more data? Enter yes or no.\n')

    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_user(df)

        
        


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
