'''
Write a program that require to user type the hour and return greeting
'''

hour = input("What time is it?")

if hour.isdigit():
    hour = int(hour)
    if hour < 0 or hour > 23:
        print("The hour must to be between 0 and 23")
    else:
        if hour <= 11:
            print("Good Morning")
        elif hour <= 17:
            print("Good Afternoon")
        else:
            print("Good evening")
else:
    print("Write the value between 0 and 23")