# NAME OF AUTHOR: Ariana Hrlic
# NAME OF THE PROGRAM:  Q2 Average
# DATE OF CREATION: January,19,2022
# PURPOSE OF PROGRAM: collects a series of non zero numbers and caluclates the sum and average of them  


# VARIABLE DEFINITION

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
input("please enter the number 0 to see your sum and average")

sum = int(0 + userList) 

#average = userList // 


# OUTPUT

if input == 0: 
  print(sum)

#if input == 0:
  #print(average)
