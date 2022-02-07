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
    print('Hello! what about exploring some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Enter city name chicago, new york city or washington : ').lower()
    while city not in CITY_DATA.keys():
        print('please enter a valid city from chicago, new york city or washington ')
        city=input('Enter city name chicago, new york city or washington : ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','all']
    month=input('which month you like to explore from january,february,march,april,may,june or all : ').lower()
    while month not in months:
        print('please enter a valid month from january,february,march,april,may,june or all')
        month=input('which month you like to explore from january,february,march,april,may,june or all : ').lower()      
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    day=input('which day do you like to explore from saturday,sunday,monday,tuesday,wednesday,thursday,friday or all : ')
    while day not in days:
        print('please enter a valid day of week from saturday,sunday,monday,tuesday,wednesday,thursday,friday or all')
        day=input('which day do you like to explore from saturday,sunday,monday,tuesday,wednesday,thursday,friday or all : ')
    print('*'*40)
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
    df=pd.read_csv(CITY_DATA[city]) #read csv file for selected city 
    df['Start Time']=pd.to_datetime(df['Start Time']) #convert data to date and time 
    df['month']=df['Start Time'].dt.month #extract month from Start time column
    df['day of week']=df['Start Time'].dt.weekday_name #extract day name
    df['start hour']=df['Start Time'].dt.hour #extract start hour 
    if month !='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day !='all':
        df=df[df['day of week']==day.title()]
    return df

def display_raw_data(df):
    """
    asking the user if he/she would like to display first 5 from the data ...
    """
    index=0
    user_index=input('do you like to display first 5 rows of data ? yes or no : ').lower() #convert user input to lower case
    if user_index not in ['yes','no']:
        print('please enter a valid choice yes or no')
        user_index=input('do you like to display first 5 rows of data ? yes or no : ').lower()
    elif user_index == 'no':
        print('let\'s continue..')
    else:    
        while index+5<df.shape[0]:
            print(df.iloc[index:index+5])
            index+=5
            user_index=input('do you like to display next 5 rows of data ? yes or no : ').lower()
            if user_index!='yes':
                print('let\'s continue')
                break
                                     
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print('the most common month : ',most_common_month)
    # TO DO: display the most common day of week
    most_common_day=df['day of week'].mode()[0]
    print('the most common day : ',most_common_day)
    # TO DO: display the most common start hour
    most_common_start_hour=df['start hour'].mode()[0]
    print('the most common start hour : ',most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    most_commonly_startstation=df['Start Station'].mode()[0]
    print('the most commonly used start station is ',most_commonly_startstation)
    # TO DO: display most commonly used end station
    most_commonly_endstation=df['End Station'].mode()[0]
    print('the most commonly used enf station is ',most_commonly_endstation)
    # TO DO: display most frequent combination of start station and end station trip
    print('the most frequent combination is Start station ',most_commonly_startstation,'and end station is ',most_commonly_endstation)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total time travel ',total_travel_time/3600,' hrs')
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('total time travel ',mean_travel_time/3600,' hrs')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user=df['User Type'].value_counts()
    print('counts of usrt types \n',counts_of_user)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_of_gender=df['Gender'].value_counts()
        print('counts of gender \n',count_of_gender)
    else:
        print('no gender column in this data set')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year_of_birth=int(df['Birth Year'].min())
        recent_year_of_birth=int(df['Birth Year'].max())
        most_common_year_of_birth=int(df['Birth Year'].mode()[0])
        print('earliest year of birth is : ',earliest_year_of_birth)
        print('most recent year of birth is : ',recent_year_of_birth)
        print('most common year of birth is : ',most_common_year_of_birth)  
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print('no birth year column in this data set')
        print('*'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        # time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()
