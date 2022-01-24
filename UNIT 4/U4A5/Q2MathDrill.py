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
answer2 = 0
number3 = 0
number4 = 0

#input

decider = random.randint(1,2)  

while True:

  if decider == 1:

    number1 = (random.randint(1, 12))
    number2 = (random.randint(1, 12))

  print(number1, number2)
  print("please answer the multiplication question:")
  userAnswer = int(input())


#output
  answer = int((number1 * number2))
  answer = (str(answer))

  if userAnswer == answer: 
    print("you are correct! ")
  elif userAnswer != answer:
    print(("Incorrect, The answer to this question was actually ") + answer)


  if decider == 2:

    number3 = (random.randint(1, 100))
    number4 = (random.randint(1, 100))

  print(number3, number4)
  print("please answer the addition question:")
  userAnswer = int(input())

  answer2 = int((number1 + number2))
  answer = (str(answer))
  
  if userAnswer == answer2: 
    print("you are correct! ")
  elif userAnswer != answer2:
    print(("Incorrect, The answer to this question was actually") + answer2)

  x = exit(input("if you would like to exit the game please enter x:"))  