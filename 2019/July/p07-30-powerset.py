#!/bin/python

#ok Note To self may need to write this code in more iterative format.
# generator format rather than build power set in one go format.
#ok maybe this solution needs to work out a little more complicated. 


#a power set is a set which contains all possible subsets from a set. 
#starting with biggest sizes first. 
# the problem becomes when you need to 
def generatePowerSet(list):
    powerset = [[]]
    currentSize = 1
    whichPositonMoveForward = 0
    currentPositions = [];
    while currentSize < len(list):
        currentPosition.add(len(currentPositions));
        whichPositonMoveForward = len(currentPositions)
        while whichPositonMoveForward > -1:
            while currentPosition[whichPositonMoveForward] < len(list): 
                powerset.add(generateSetFromPositons(list,currentPositions))
                currentPosition[whichPositonMoveForward] += 1 
        whichPositonMoveForward -= 1;
    
                    
        

def generateSetFromPositons(list,currentPositions):
    pset = []
    for item in currentPositions: 
        pset.append(list[item])
    return pset;
    
#my first idea was to solve for all slices.
# which in theory would cover the vast majority of 
# cases however this wouldnt work. 

# 



if __name__ == "__main__":
    positions=[1,2]
    set=[1,2,3]
    print(generateSetFromPositons(set,positions))