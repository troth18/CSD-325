import csv
#Change 1: Imported sys for exit option
import sys
from datetime import datetime
from matplotlib import pyplot as plt

#Change 2: Added instructions for how to use the program
print('''To use this program, please enter either High to see high temperatures, 
Low to see low temperatures, or Exit to exit the program.''')

#Change 3: Added a get_input function to handle user input
#Loops until user enters Exit
def get_input():
#Loop for user input
    while True:
            user_input = input('Enter High, Low, or Exit: ')
            if user_input.upper() == 'HIGH':
                print('Here is the temperature highs for 2018.')
                get_highs()
            elif user_input.upper() == 'LOW':
                print('Here is the temperature lows for 2018.')
                get_lows()
            elif user_input.upper() == 'EXIT':
                print('Thank you for choosing Sitka, come again!')
                sys.exit()
            else:
                 print('Invalid input. Please enter High, Low, or Exit.')

#Change 4: Added a get_highs function that's called when user enters High
#Moved the with open into function to prevent file from closing
#before data could be accessed
#Moved the high temperatures plot into function to allow for low
#temperatures plot
def get_highs():
# Get dates and high temperatures from csv file.
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    
        dates, highs = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)

    # Plot the high temperatures.
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

#Change 5: Added a get_lows function that's called when user enters Low
#Added second with open to low function
#Added low temperatures plot
def get_lows():
# Get dates and low temperatures from csv file.
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
          reader = csv.reader(f)
          header_row = next(reader)

          dates, lows = [], []
          for row in reader:
               current_date = datetime.strptime(row[2], '%Y-%m-%d')
               dates.append(current_date)
               low = int(row[6])
               lows.append(low)
    
    # Plot low temperatures
    fig, ax = plt.subplots()
    #Changes graph to blue
    ax.plot(dates, lows, c='blue')

    plt.title('Daily low temperatures - 2018', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

#Calls the get_input function
get_input()