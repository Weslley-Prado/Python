#Index

phrase = 'o rato roeu a roupa do rei de roma'
phrase_size = len(phrase)
account = 0
new_string = ''

input_of_user = input('What letter do you want capitalized? ')

while account < phrase_size:
    letter = phrase[account]
    if letter == input_of_user:
        new_string += input_of_user.upper()
    else:
        new_string += letter
    account += 1

print(new_string)