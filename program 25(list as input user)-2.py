numofWords = 0
numofLetters = 0
numofDigits = 0

n= input ("enter a text of numbers :") #My name is 123
for x in n :
    x = x.lower()
    if x >= 'a' and x <='z':
        numofLetters = numofLetters + 1

    elif x >= '0' and x <='9':
        numofDigits = numofDigits + 1

    elif x == ' ' and x <=' ':
        numofWords = numofWords + 1

print("Number of Letters",numofLetters)
print("Number of Digits",numofDigits)
print("Number of Words",numofWords + 1)