import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

year = date.strftime("%Y")
name = 'Weslley'
age: int = 27
height = 1.77
kg = 94.80
imc = kg / (height ** 2)
bornYear = int(year) - age

print(f'My name is {name}, and I am , {age}, year old.')
print(f'Kg =  {kg} ,  height =  {height},  imc = {imc: .2f}')
print(f'I born in {bornYear}')
