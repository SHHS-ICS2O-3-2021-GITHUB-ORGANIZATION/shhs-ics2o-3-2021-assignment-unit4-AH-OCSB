#Name: Ariana Hrlic
#Date of Creation: January 24, 2022
#Name of program: Guess Number Game 
#purpuse of program: allow user to chose a range and guess which number which was randomly selected
#
import random

#variables

userAnswer = 0
minimunNumber = 0
maximumNumber = 0
answer = 0 
counter = 0 
userAnswer = 0
turn = 0

#input
minimunNumber = int(input("please enter the minimum number you would like the random number to be between:"))

maximumNumber = int(input("please enter the maximum number you would like the random number to be between:"))

answer = random.randint(minimunNumber, maximumNumber) 

while turn == 0:

  userAnswer = int(input("please guess a number between the range that you had specified "))

  if userAnswer == answer: 
    print("You win! Youve guessed the number correctly")

    turn = 1 

#counts how many times it took the user and tells them
    counter = counter + 1
    
    counter = (str(counter))
    print(("You won! \n the numbers of tries you took was: ") + counter)
    exit()
    elif(userAnswer != answer)
    print("You did not win :( ")

    counter = counter + 1 

    print("try again!")