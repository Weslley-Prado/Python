# Area Rectangle

sideRectangleA = float(input("Type a value: "))
sideRectangleB = float(input("Type a value: "))
areaRectangle = sideRectangleA * sideRectangleB

print(f"The are of the rectangle is {areaRectangle} m²")


# Area Square

sideSquareA = float(input("Type a value: "))
sideSquareB = float(input("Type a value: "))
areaSquare = sideSquareA * sideSquareB

print(f"The are of the square is {areaSquare} m²")

# Discount example

valueProduct = float(input("Type a value: "))
valueDiscount = float(input("Type a value: "))
priceWithDiscount = valueProduct - (valueProduct*valueDiscount/100)

print(f"The value of product is {priceWithDiscount} ")
