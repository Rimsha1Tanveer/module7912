city=input("Enter your city name:")
temp=float(input("Enter today's temperature:"))

if temp>35:
    print("Warning: Its very hot today!")

if temp>25:
    print("Great day to go outside!")
else:
    print("Its a cold outside.")
    

if temp>35:
    print("Its very hot")
    
elif temp>25:
    print("Great weather!")
elif temp>15:
    print("Its a bit cold")
else:
    print("Stay warm")
    
import datetime
import calendar

now=datetime.datetime.now()
print("Current date and time:",now)
print(calendar.calendar(now.year))