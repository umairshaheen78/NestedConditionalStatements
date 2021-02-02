'''
2/01/2021

Nested Conditional Statement:
- A conditional statement inside another conditional statement

Indentation
- The header/clause of a nested conditional statement must be indented from an outter header.

if (condition):
   Body statement 1
  if (condition):
    Body statement 1a <-- ending a nested statement

elif (Condition): <--- starting a nested statement
  Body statement 2b

 else:
    Body statement 2c <-- ending a nested statement

else:
  Body Statement3

# Example:
x = y = 10
if (x < y):
 print ("x is less than y!")
else:
  if (x > y):
    print ("x is greater than y!")
  else:
      print ("x and y must be equal!")
  
'''

# Exercise: Evaluate if your number is positive/negative/zero and if it is odd and even.
# ----------------------------------------------
num = int(input("Enter a number: "))
if (num > 0):
  if (num % 2 == 0):
    print ("Your number is even and your number is positive!")
elif (num < 0):
  print ("Your number is negative!")
if (num == 0):
  print ("You have entered the number zero!")
