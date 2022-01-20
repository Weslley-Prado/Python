'''
Write a program that require to user type an int number, and show if it's int or not
and if it's even and odd too.
'''

number = input('Write an integer number, please: ')
print()
if not number.isdigit():
    print("It isn't integer number")
else:
     number = int(number)
     if not number % 2 == 0:
          print(f"{number} it's even")
     else:
          print(f"{number} it's par")

