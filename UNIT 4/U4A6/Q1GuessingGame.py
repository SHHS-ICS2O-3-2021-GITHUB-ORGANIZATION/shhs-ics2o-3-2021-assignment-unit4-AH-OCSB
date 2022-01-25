#Name: Ariana Hrlic
#Date of creation: January, 25, 2022
#Name of program: Guess Number Game
#Purpose of program: All user to guess number between a range they specify 

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
#allows user to input their own range, minimum number and maximum number
minimunNumber = int(input("please enter the minimum number you would like the random number to be between:"))

maximumNumber = int(input("please enter the maximum number you would like the random number to be between:"))

answer = int(random.randint(minimunNumber, maximumNumber))
#allow user to continue to guess untill they guess the number correctly 
while turn == 0:

  userAnswer = int(input("please guess a number between the range that you had specified "))

#output 
  if userAnswer == answer: 
    counter = counter + 1
    print("You win! Youve guessed the number correctly")
    counter = (str(counter))
    print(("You won! \n the numbers of tries you took was: ") +(counter))
    turn = 1
  else:
      print("You did not win :( ")
#counts how many times it took the user and tells them
      counter = counter + 1 

      print("try again!")


      turn = 0

  
    
  
    