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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Which city do you want to see Chicago, New York or Washington?")
    city_name=['Chicago','New York','Washington']
    while True:
          city= input().title()
          if city in city_name:
             print("Ok so {} !!".format(city))
             break
          else:
             print("Please make sure you entered the right value :)")
             continue

    # get user input for month (all, january, february, ... , june)
    print("Please write the name of the month you want to filter by, or you can write (All) to apply no month filter")
    months= ['January', 'February', 'March', 'April', 'May', 'June'] 
    while True:
          month = input().title()
          if month == 'All':
             print("Ok so no month filter") 
             break
          elif month in months:
             print("We will filter by {} !!".format(month))
             break  
          else:
             print("Please make sure you entered the right value :)")
             continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("Please write the name of the day you want to filter by, or you can write (All) to apply no day filter")
    days= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    while True:
          day = input().title()
          if day == 'All':
             print("Ok so no day filter") 
             break
          elif day in days:
             print("We will filter by {} !!".format(day))
             break  
          else:
             print("Please make sure you entered the right value :)")
             continue  


    print('-'*100)
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
    #load data into a dataframe
    df=pd.read_csv(CITY_DATA[city])

    #convert start time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    #take day and month from start time then make a new column
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.day_name()

    #filter by month
    if month != 'all':
       months= ['january', 'february', 'march', 'april', 'may', 'june'] 
       month= months.index(month) + 1

       #create the new dataframe
       df=df[df['month'] == month]

    #filter by day
    if day != 'all':
       #create the new dataframe
       df=df[df['day_of_week'] == day.title()]   
       
    return df
    

def time_stats(df):
   """Displays statistics on the most frequent times of travel."""

   print('\nCalculating The Most Frequent Times of Travel...\n')
   start_time = time.time()

   # display the most common month
   df['month']= df['Start Time'].dt.month
   most_common_month= df['month'].mode()[0]
   print('Most Common Month:', most_common_month)

   # display the most common day of week
   df['day_of_week']= df['Start Time'].dt.day_name()
   most_common_day= df['day_of_week'].mode()[0]
   print('Most Common Day:', most_common_day)

   # display the most common start hour
   df['hour']= df['Start Time'].dt.hour
   most_common_hour= df['hour'].mode()[0]
   print('Most Common Hour:', most_common_hour)

   #Prints how much time it took the program to do the calculation
   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*100)


def station_stats(df):
   """Displays statistics on the most popular stations and trip."""

   print('\nCalculating The Most Popular Stations and Trip...\n')
   start_time = time.time()

   # display most commonly used start station
   most_common_start_station= df['Start Station'].mode()[0]
   print("Most commonly used start station: ", most_common_start_station)
    
   # display most commonly used end station
   most_common_end_station= df['End Station'].mode()[0]
   print("Most commonly used end station: ", most_common_end_station)

   # display most frequent combination of start station and end station trip
   df['Combined'] = df['Start Station'] + " + " + df['End Station']
   frequent_combination= df['Combined'].mode()[0]
   print("The most frequent combination of start station and end station trip: ",frequent_combination)

   #Prints how much time it took the program to do the calculation
   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*100)


def trip_duration_stats(df):
   """Displays statistics on the total and average trip duration."""

   print('\nCalculating Trip Duration...\n')
   start_time = time.time()

   # display total travel time
   total_travel_time= df['Trip Duration'].sum()
   print("Total Trip Duration: ",total_travel_time)
    
   # display mean travel time
   mean_travel_time= df['Trip Duration'].mean()
   print("Average Trip Duration: ",mean_travel_time)

   #Prints how much time it took the program to do the calculation
   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*100)


def user_stats(df):
   """Displays statistics on bikeshare users."""

   print('\nCalculating User Stats...\n')
   start_time = time.time()
   
   # Display counts of user types
   user_types= df['User Type'].value_counts()
   print(user_types)
   try:
      # Display counts of gender
      user_gender= df['Gender'].value_counts()
      print(user_gender)

   except:
      print("There is no gender data for this city")

   try:
      # Display earliest, most recent, and most common year of birth
      earliest_year= int(df['Birth Year'].min())
      print("The erliest year of birth: ",earliest_year)
      
      recent_year= int(df['Birth Year'].max())
      print("The most recent year of birth: ",recent_year)

      common_year= int(df['Birth Year'].mode()[0])
      print("The most common year of birth: ",common_year)

   except:
      print("There is no birth year data for this city")
      
   
   #Prints how much time it took the program to do the calculation
   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*100)


def show_raw_data(df):
   """ function to display 5 lines of raw data"""

   print("Would you like to see raw data? (yes) or (no)")
   answer= input().lower()
   while True:
      if answer == 'yes':
         print(df.head())
         break
      elif answer == 'no':
         print("")
         break
      else:
         print("Please answer with (yes) or (no)")
         show_raw_data(df)
         return

   print('-'*100)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
