age = int(input("Type your age "))

if age == 5 or age <= 7:
    print("Infantil A")
elif age == 8 or age <= 10:
    print("Infantil B")
elif age == 11 or age <= 13:
    print("Juvenil A")
elif age == 14 or age <= 17:
    print("Juvenil B")
else:
    print("Type age between 7-17")
