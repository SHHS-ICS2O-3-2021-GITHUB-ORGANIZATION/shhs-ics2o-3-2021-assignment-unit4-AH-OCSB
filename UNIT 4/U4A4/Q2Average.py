# NAME OF AUTHOR: Ariana Hrlic
# NAME OF THE PROGRAM:  Q2 Average
# DATE OF CREATION: January,19,2022
# PURPOSE OF PROGRAM: collects a series of non zero numbers and caluclates the sum and average of them  


# VARIABLE DEFINITION
import math

list = 0

userList = 0

# INPUT

list = input("please enter the series of numbers separated by a space: ")

#split makes the string of numbers into a list
userList = list.split()

# PROCESSING

for i in range(len(userList)):
  userList[i] = int(userList[i])

#allowing the user to see their average and sum of the numbers 
zeroInput = int(input("please enter the number 0 to see your sum and average"))

#average = userList // 
listLength = len(userList)
listSum = sum(userList)
listAverage = listSum//listLength
# OUTPUT

if zeroInput == 0: 
   print("Sum = ", listSum)
   print("average = ", listAverage)
elif zeroInput != 0:
  zeroInput2 = int(input("please try again: "))
  if zeroInput2 == 0: 
    print("sum =", listSum)
    print("average = ", listAverage)
  else:
      print("You Failed")
      exit()