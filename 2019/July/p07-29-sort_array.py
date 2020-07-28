#!/bin/python

# Given an array of strictly the characters 'R', 'G', and 'B', 
# segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

# ok, have an idea for solving this one. 
# so we are gonna need three loops
#first loop setups all the Rs on the right side. 
#the second sets up the Gs 
#third setups any remaing B characters
#if possible, later make this strategy more generic by allowing more characters divisions in array, 
#up to arbiritrary amount.
# Swap function 



#now this works in O(n) time, with constant Space.
#you could make it work with more complicated setups, allowing for lists of items in array.
# in theory, you could have this work with arbitrary lists.
# with that, it will work in O(n*d),
# d being the number of divisions. 
def SortRGB(array,characterList=['R','G','B']):
    currentElem = 0;
    endOfSort = 0;
    while currentElem < len(characterList) and endOfSort < len(array):
        currentPoint = endOfSort;
        while currentPoint < len(array):
            if array[currentPoint] == characterList[currentElem]:
                if currentPoint > endOfSort: # reduces swapping in case partial sorted are in front not neccessary improvent!
                    swapPositions(array,currentPoint,endOfSort)
                    print("swapped", currentPoint, endOfSort, sep=" : ")
                endOfSort += 1
            print(array , "\n")
            currentPoint += 1;
        currentElem += 1;
    
    
           
def sortForward(array,endOfSort,character):
    
    return endOfSort;
 
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
    
if __name__ == "__main__":
    # test = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    # print(SortRGB(test))
    # test = ['R','R','R','R']
    # print(SortRGB(test))
    test = ['B','R','R','R']
    print(SortRGB(test))