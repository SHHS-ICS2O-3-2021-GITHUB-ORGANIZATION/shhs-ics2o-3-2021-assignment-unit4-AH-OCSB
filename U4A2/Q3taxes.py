# NAME OF AUTHOR: Ariana Hrlic
# NAME OF THE PROGRAM: Item cost 
# DATE OF CREATION: January,12,2022
# PURPOSE OF PROGRAM: Calculate the cost of 10 items with tax included


# VARIABLE DEFINITION

ItemCost1 = 0
ItemCost2 = 0
ItemCost3 = 0
ItemCost4 = 0
ItemCost5 = 0
ItemCost6 = 0
ItemCost7 = 0
ItemCost8 = 0
ItemCost9 = 0
ItemCost10 = 0 

Tax = float(0.13)

TotalCost = 0

# The last "t" in the variable TotalCosT is refering to the total cost with tax, this variable is different from the one above - "TotalCost" 
TotalCosT = 0

# INPUT

ItemCost1 = float(input("please enter the cost of item one:"))
ItemCost2 = float(input("please enter the cost of item two:"))
ItemCost3 = float(input("please enter the cost of item three:"))
ItemCost4 = float(input("please enter the cost of item four:"))
ItemCost5 = float(input("please enter the cost of item five:"))
ItemCost6 = float(input("please enter the cost of item six:"))
ItemCost7 = float(input("please enter the cost of item seven:"))
ItemCost8 = float(input("please enter the cost of item eight:"))
ItemCost9 = float(input("please enter the cost of item nine:"))
ItemCost10 = float(input("please enter the cost of item ten:"))


# PROCESSING

TotalCost = (ItemCost1 + ItemCost2 + ItemCost3 + ItemCost4 + ItemCost5 + ItemCost6 + ItemCost7 + ItemCost8 + ItemCost9 + ItemCost10)

TotalCosT = (TotalCost * Tax)


# OUTPUT

print("The total cost with out Tax is:")
print(TotalCost)
print("The total cost with Tax is:") 
print(TotalCosT)
