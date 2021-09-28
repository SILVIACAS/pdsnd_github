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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input('\n Which cities do you want to explore?: chicago, new york city or washington \n').lower().title()
        if city in CITY_DATA:
            break
        else:
            print('\n The information of that city is not avaible, choose another one')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        months = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'november','all')
        month = input('\n Which month would you like to analyze? Type "all" in case you do not want to filter the data \n').lower().title()
        if month in months:
            break
        else:
            print('\n The information of that month is not avaible, choose another one')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        days = ('monday','tuesday','wednesday','thursday','friday', 'all')
        day = input('\n Which day of the week would you like to analyze? Type "all" in case you do not want to filter the data \n').lower().title()
        if day in days:
            break
        else:
            print('The information of that month is not avaible, choose another one')

        return city, month, day

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    month = df['Start Time'].dt.month
    common_month = month.mode()[0]
    calendar_month_name = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
    print('Most Common month is:', calendar_month_name[common_month - 1])

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    week_day = df['Start Time'].dt.weekday_name
    common_week_day= week_day.mode()[0]
    print('Most Common day of the week to travel is:', common_week_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    hour = df['Start Time'].dt.hour
    common_hour = hour.mode()[0]
    print('Most Common hour is:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common Start Station is:',common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common End Station is:',common_end)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time in seconds is:', total_time)

    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print('The average travel time in seconds is:', average_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('Distribution of User Type:',user_count)

    # TO DO: Display counts of gender
     if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('Distribution of gender in Chicago:',gender_count)
    else:
        print('Gender does not appear in the dataframe')
<<<<<<< HEAD

=======
        
>>>>>>> refactoring

    # TO DO: Display earliest, most recent, and most common year of birth
    if city is not 'washington':
        recent_birth = df['Birth Year'].max()
        print('The most younger user was born in:',recent_birth)
    else:
        print('Birth Year does not appear in the dataframe')

    if 'Birth Year' in df:
        earlist_birth = df['Birth Year'].min()
        print('The oldest user was born in:',earlist_birth)
    else:
        print('Birth Year does not appear in the dataframe')

    if 'Birth Year' in df:
        common_birth = df['Birth Year'].mode()[0]
        print('The most common birth date is:',common_birth)
    else:
        print('Birth Year does not appear in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def rows():

    while True:
    rows = input('\n Would you like to see 5 rows of data? Enter yes or no \n').lower()
    start_loc = 0
    if rows == 'yes':
        print(df.iloc[0:5])
        start_loc += 5
        display = ('\n Would you like to continue? Enter yes or no \n').lower()
        if display == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
