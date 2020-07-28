#!/bin/python



# Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

# For example, given the following tree and K of 20

    # 10
   # /   \
 # 5      15
       # /  \
     # 11    15

# Return the nodes 5 and 15.

def sumOfTwoNodes(list,sum):
   # to find two Nodes that equal sum. 
   # ok, brute force solution
   # works by programmaticaly working thru all combinations?
   
   # if this was an array
   index1 = 0
   index2 = 1
   closestPair = [0,1]
   closestDistance = 1000000 # it really doesnt matter as long as it is bigger than 99 percent of numbers
   while index1 < len(list)-1:
        index2 = index1 + 1 
        while index2 < len(list):
               
                return [index1,index2] 
            index2 += 1
        index1 += 1
    
def sumOfTwoNodesBTree(BTree,sum):
    # is there a way to start near the closest pair and work your way towards it?
    # ok I think I have the way to do it. 
    # start at the highest pair and work your way down. 
    # once all pairs are smaller than the target you dont need to look further.
    # relationship should always be Primary >= secondary
    primary = findLargetNode(Btree);
    secondary = findNodeBelowOrEqualTo(Btree,node1.value);
    while True:
          summedValue =  primary.Value + secondary.Value;
          if summedValue = sum:
            return [primary,secondary]
          if summedValue > sum:
                secondary = findNodeBelowOrEqualTo(Btree,secondary.value)


def findLargetNode(BTree):
    currentNode = BTree
    lastNode = BTree
    while CurrentNode != None:
        lastNode = currentNode
        currentNode = currentNode.right;
    return lastNode


# screwed up, this is supposed to find that is just below 
# the target value but it doesnt have to find the exact value. 
def findNodeBelowOrEqualTo(BTree,sum):
    currentNode = BTree
    LastNode= BTree
    while currentNode != None:
        if currentNode.Value < sum:
            lastNode=CurrentNode;
            currentNode = currentNode.right;
            if currentNode = sum:
                return currentNode;
        if CurrentNode > sum:
            lastNode = currentNode;
            currentNode = currentNode.left;
    return lastNode;
        
            
if __name__ == "__main__":
    print(function())