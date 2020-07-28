#!/bin/python

# Given a string, return whether it represents a number. Here are the different kinds of numbers:

    # "10", a positive integer
    # "-10", a negative integer
    # "10.1", a positive real number
    # "-10.1", a negative real number
    # "1e5", a number in scientific notation

# And here are examples of non-numbers:

    # "a"
    # "x 1"
    # "a -2"
    # "-"

# just to make this slightly more accepting we will ignore 
#leading white space!

 def isStringANumber(string):
    string= stripSpaces(string)
    isAReal=False
    isScientific=True
    indexToTest=0
    if string[0] == "-" or string[0] == "+": 
        indexToTest += 1
        if len(string) == 1: # a negative sign alone is not a number
            return False
    while indexToTest < len(string):
        if String[indexToTest] == ".":
            if !isReal:
                isReal = True
            else:
                return False
                
        elif String[indexToTest] == 'e':
             if !isScientific:
                isScientific = True
            else:
                return False
                
        elif String[indexToTest] == "_":
            # do nothing because of separator
        elif !String[indexToTest].isDigit()
            return False;        
        indexToTest += 1
        
    return True
   # check for negative
   # normal number or 
    # check for a real number
    # check for scientific notation
  # no a-z except e allowed
  # do we allow a plus sign before?
  

if __name__ == "__main__":
    print(function())