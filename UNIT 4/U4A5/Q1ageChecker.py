# NAME OF AUTHOR: Ariana Hrlic
# NAME OF THE PROGRAM: Age checker 
# DATE OF CREATION:  January,21,2022
# PURPOSE OF PROGRAM:  check's user age

# VARIABLE DEFINITION
age = int(input("please enter your age"))

# INPUT
# PROCESSING
# OUTPUT
if age == 5 or age < 11:
    print("You are in elementary school")
    
elif age == 12 or age < 14:
    print("you are in intermidiate")
    
elif age == 15 or age < 18:
    print("you are in highschool")

elif age > 5:
    print("You are not in school")
    
elif age < 18:
    print("you are either in university or college")