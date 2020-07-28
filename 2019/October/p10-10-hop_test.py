#!/bin/python
# this 10/8 problem
# Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

#ok if we are on a 1 step problem 
# no additional tests need to be doneS
def hopTest(list):
    numOfMoves =hopTestR(list,0,0)
    return numOfMoves 
# we need to signal two pieces  of info
# we return number of moves? 
# -1 is impossible to move Forward 
def hopTestR(list,currentSpot,numOfMoves): 
    if currentSpot >= len(list)-1:
        return numOfMoves
    elif  list[currentSpot] == 0:
        return -1;
    elif list[currentSpot] == 1:
        return hopTestR(list,currentSpot+1,numOfMoves+1)
    else:
        currentHopTest = list[currentSpot]
        while currentHopTest > 0:
           numOfHops = hopTestR(list,currentSpot+currentHopTest,numOfMoves+1)
           if numOfHops != -1:
                return numOfHops;
        currentHopTest -= 1
        return -1
        
        
if __name__ == "__main__":
    print(hopTest([2, 0, 1, 0])) # 2
    print(hopTest([1, 1, 0, 1])) # -1
    print(hopTest([3, 0, 0, 0])) # 1
    print(hopTest([3, 0, 0]))    # 1
    