#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
n = input("Enter a number smaller than 10: ")
n=int(n)

if n >= 10:
    print("SMALLER NUNBER THAN 10")
else:
    sum = 0
    yb =0 
  
    for i in range(1, n + 1):
        yb = yb * 10 + 1
        sum = sum + yb

    print(f"The sum of the series is {sum}")




            
  
      
