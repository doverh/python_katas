# Exercise from https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Requirements
# Receive an user input as integer
# 1. Is it a number?
# 2. Is it even? Divide by 2 with no remaider from division
# Extra 1. Is it also divided by 4
# Extra 2. Receive 2 numbers, first input is num, second input is the divisor, call it "check". 
# Inform the user the appropriate result - divisible or not 

#solution
#Convert string input in a int
#class Katas(object):
#def __init__(self):
#print('instance method called', self)
        
#@classmethod    

def isNumberEven(userInput):
    try:
        num = int(userInput)
        if((num % 2) == 0):
            return("This number is even")
        else:
            return("This number is odd")
    except ValueError:
        return("Please enter a number")

