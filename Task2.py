"""
Zar Jerome C. Cajudo
Task 2
"""

#Libraries and Functions always come in handy to developers by allowing reusability of existing code.
#There are certain well known inherent libraries that you have access to after installing python.
#By using these libraries and functions in them,
#write a program (in Python 3) to guess a randomly generated number between 1 and 10. 

#Hint: Figure out which library the “randint” function belongs to.  

#-----------------------------------------------------------------------------------------------------
import random

a = random.randint(1,10)

while True:
    b = int(input("Please enter a number: "));
    if b == a:
        print("Correct!");   
        break
    elif b!= a:
        print("Wrong number.Try again..."); 
    

