from random import randint
import sys

def generateRandomInt():
    randomInt = randint(1,10)
    return str(randomInt)


def checkUserInputAndRandomInt(userIn, randomIn):
    if(userIn == randomIn):
        print("Your guess is correct, the number is: "+randomIn)
    else:
        print("Sorryyy!! The number is: "+randomIn)

choice = True
while choice:
    print("We have a number in mind! Let's see if you can guess it! \n Enter the number between 1 to 10:")
    userInputNum = input()
    checkUserInputAndRandomInt(str(userInputNum), generateRandomInt())

    print("enter y to continue")
    choice = ("y") in input().lower()
