'''
For in
Iterando strings with for
Function range (start=0, stop, step=1)
'''

text = 'Python'
c = 0
print('-----------------------The bad way-----------------------')
while c < len(text):
    print(text[c])
    c += 1
print('-----------------------The better way-----------------------')

for letter in text:
    print(letter)

print('-----------------------Enumerate-----------------------')

for n, letter in enumerate(text):
    print(n, letter)

print('-----------------------for with range-----------------------')

for number in range(20, 10, -1):
    print(number)

for number1 in range(10):
    print(number1)

for N in range(0, 100, 8):
    print(N)

for n in range( 100 ):
    if n % 8 == 0:
        print(n)
print('____________For with String ___________________')

text = 'Python'
new_string = ''

for letter in text:
    if letter == 't':
        continue
        new_string = new_string + letter.upper()
    elif letter == 'h':
        new_string += letter.upper()
        break
    else:
        new_string=letter
    print(new_string)
