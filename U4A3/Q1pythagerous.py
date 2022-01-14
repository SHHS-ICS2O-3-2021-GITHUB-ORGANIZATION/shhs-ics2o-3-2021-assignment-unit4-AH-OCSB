# NAME OF AUTHOR: Ariana Hrlic
# NAME OF THE PROGRAM: Pythagoream therom 
# DATE OF CREATION:  January,14,2022
# PURPOSE OF PROGRAM:  Calaculate the pythagoream therom with numbers given by the user 


# VARIABLE DEFINITION

lengthA = 0 
lengthB = 0
#lengthC is also the answer 
lengthC = 0

# INPUT

lengthA = int(input("please enter the length of side A: "))
lengthB = int(input("please enter the length of side B: "))


# PROCESSING
import math

lengthC = (lengthA**2) + (lengthB**2)



# OUTPUT

print(lengthC)