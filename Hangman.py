from os import system, name
from time import sleep

def Guess_Next_Letter(chances, wordToBeGuessed, guessedWordList):
    while(chances > 0):
        print("Number of chances left : ")
        print(chances)
        if(len(guessedWordList) != len(wordToBeGuessed)):
            print("Enter what you think is the next letter:")
            next_letter = input()
            if(next_letter != wordToBeGuessed[len(guessedWordList)]):
                print("wrong word guess again!")
                chances = chances - 1
            else:
                guessedWordList.append(next_letter)
                print("Correct!!")
                tillNowGuessedWord = ""
                for allLetters in guessedWordList:
                    tillNowGuessedWord = tillNowGuessedWord + allLetters

                print("The word that you have guessed till now is: "+tillNowGuessedWord)
                print("Guess letter number "+str(len(guessedWordList)+1))
        else:
            chances = 0
            
play = True
while play:
    
    print("Input the word to be guessed and a hint (optional)")
    wordToBeGuessed = input()
    hint = input()
    print ("\n" * 100) #for clearing screen
    print("Your hint is \""+hint.upper()+"\"" )
    lengthofWord = 0;
    guessedWordList = [wordToBeGuessed[0]]
    for letter in wordToBeGuessed:
        lengthofWord = lengthofWord + 1

    print("The length of the word is: "+str(lengthofWord))
    print("You have "+str(int(lengthofWord)+3)+" chances to guess the word")
    numberofChances = lengthofWord+3
    print("You will be shown the first letter of the word and then you have to guess the rest")
    print(wordToBeGuessed[0])
    
    Guess_Next_Letter(numberofChances,wordToBeGuessed,guessedWordList)

    guessedWord = ""
    for eachLetter in guessedWordList:
        guessedWord = guessedWord+eachLetter

    if(guessedWord == wordToBeGuessed):
        print("Hurrahhh!! You guessed it: ")
        print("The answer is : " + guessedWord)
    else:
        print("Sorry! The hangman is dead !!! Answer is: "+ wordToBeGuessed)
    



    #end statement
    print("enter y to continue")
    play = ("y") in input().lower()
    
    
