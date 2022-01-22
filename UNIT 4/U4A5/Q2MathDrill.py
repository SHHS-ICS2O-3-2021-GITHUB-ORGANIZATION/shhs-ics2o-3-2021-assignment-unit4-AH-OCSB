#Name of creator: Ariana Hrlic
#Date of Creation: January,21,2022
#Name of Creation: Math problem Generator
#Purpuse of the program: Generate a multiplaction problem with random generated numbers


import random 

#variables
number1 = 0
number2 = 0
question = 0
answer = 0

#input
while True:
  number1 = (random.randint(1, 12))
  number2 = (random.randint(1, 12))

  print(number1, number2)
  print("please answer the multiplaction question:")
  userAnswer = int(input())


#output
  answer = int((number1 * number2))

  if userAnswer == answer: 
    print("you are correct! ")
  elif userAnswer != answer:
    print("Incorrect, The answer to this question was actually") + str(print(answer))

  x = exit(input("if you would like to exit the game please enter x:"))  