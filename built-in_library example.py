# Python built-in libraies

# Import the datetime library to use it in the program
import datetime

# Assign the current date and time to a variable
time = datetime.datetime.now()
month = time.month

# Display the month with string
month_word =time.strftime("%B")

# Display date/time
print(f"The current date and time is {time}")

# Display month
print(f"The current month is {month}")
print(f"The current month is {month_word}")

# Test
today = datetime.datetime.today()
print(f"Today is {today}")

# Display the day of the week
weekday = today.weekday()
print(f"The day of the week is {weekday}")

# Gets the type of variable
print(type(weekday))
print()

'''
# Get day of week from user as integer
weekday = int(input("Enter an integer 0-6 as the day of the week: "))
'''

# If-else statements to determine the day of the week
if weekday == 0:
    weekday_word = "Monday"
    
elif weekday == 1:
    weekday_word = "Tuesday"
    
elif weekday == 2:
    weekday_word = "Wednesday"
    
elif weekday == 3:
    weekday_word = "Thursday"
    
elif weekday == 4:
    weekday_word = "Friday"

elif weekday == 5:
    weekday_word = "Saturday"

elif weekday == 6:
    weekday_word = "Sunday"

else:
    print("Invalid day of week!!!")
    weekday_word = "INVALID"
    
print()

print(f"The day of the week is {weekday_word}")






