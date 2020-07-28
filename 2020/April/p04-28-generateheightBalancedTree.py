#!/bin/python
# This problem was asked by Etsy.

# Given a sorted array, convert it into a height-balanced binary search tree.


#I have a simple idea for this probably not the fastest idea but should work. 
# you can use red-black tree or AA, I think however. 
#my alothirim is really simple. 
# it's kinda like binary search alogorithim. 
# start in the middle 

# does have at least one disadvantage takes at least O(n) time which is expected. 
# but I think also takes an additional O(N) memory! well actually O(N/2) but it doesnt matter. 
# it definetly I think you could reduce memory foot print but I am not sure if you get it to only use O(1) memory. 
def GenerateTreeFromArray(array):
    #create bass 
     middle = len(array)/2;
     generateTreeFromArray(array[0:middle],nodeToAddTo);
        generateTreeFromArray(array[middle:len(array)-1],nodeToAddTo);

def GenerateTreeFromArrayR(array,nodeToAddTo):
     if len(array) = 1:
        return;
    else: 
        middle = len(array)/2;
        #insert in the middle. 
        if array[middle] > nodeToAddTo.value:   
            nodeToAddTo.Right = new Node(array[middle]);
            nodeToAddTo = nodeToAddTo.Right
        else:  
            nodeToAddTo.Left = new Node(array[middle]);
            nodeToAddTo = NodeToAddTo.left;
       # do this for both sides 
        generateTreeFromArray(array[0:middle],nodeToAddTo);
        generateTreeFromArray(array[middle:len(array)-1],nodeToAddTo);
        
        
   

if __name__ == "__main__":
    print(function())