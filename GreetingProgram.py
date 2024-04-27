import time

timespan = time.strftime('%H:%M:%S')
print(timespan)
name = input("Enter your name: ")

hour = int(time.strftime('%H'))

if (hour > 4 and hour < 12):
    print("Good Morning,", name)
elif (hour > 12 and hour < 15):
    print("Good AfterNoon,", name)
elif (hour > 15 and hour < 18):
    print("Good Evening,", name)
else:
    print("Good Night,", name)
