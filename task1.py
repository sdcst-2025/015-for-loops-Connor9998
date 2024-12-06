#!python3 

"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
hint:
using a print statement with the optional parameter:
,end="" 
will help you print things on the same line.

Example:
print("Hello", end="")
print("This is on the same line")
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""

x=input("Enter a integer:")
#convert to a number

print((int(x)*1),(int(x)*2),(int(x)*3),(int(x)*4),(int(x)*5),(int(x)*6),(int(x)*7),(int(x)*8),(int(x)*9),(int(x)*10),(int(x)*11),(int(x)*12))