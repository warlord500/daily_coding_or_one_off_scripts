#!/bin/python

# Given two strings A and B, return whether or not A can be shifted some number of times to get B.

# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.


# the shift code is pulled from 
# https://www.geeksforgeeks.org/string-slicing-python-rotate-string/

# could you do it any  faster than O(n)?
# i dont think you could
def canShiftToGetString(src,dest):
   # you could optimize to check if they contain all the same letters before shifting?
   # save the shiftString so that you dont have to do shift work multiple times
   numberOfShifts = 1
   maxNumberOfShifts = len(src)
   shiftedString = src
   while numberOfShifts < maxNumberOfShifts:
        shiftedString = shiftString(shiftedString);
        print("shiftedString: " + shiftedString)
        if shiftedString == dest:
            return numberOfShifts;
        numberOfShifts += 1
   return -1;
    
# this rotates Left
# assumes string len is bigger than 2    
def shiftString(string):
    firstChar = string[0]
    lastPart = string[1:len(string)]
    return lastPart + firstChar
    
if __name__ == "__main__":
    print(canShiftToGetString("abc","cab"))
    print(canShiftToGetString("abcde","deabc"))
    print(canShiftToGetString("abcde","cdeab"))
    print(canShiftToGetString("abc", "acb"))