from random import randint


for x in range(1,7) :
    guessNumber = int (input("enter your guess between 1 to 5 : "))
    randomNumber = randint(1,5)
    if guessNumber == randomNumber:
        print("you have won")
    else:
        print("you have lost")
        print("Random number was: ",randomNumber)