#!/bin/python

# Given the root to a binary search tree, find the second largest node in the tree.
# hopefully, to avoid having to write the insertion algothirim of a binary tree. 
# not that i cant do that, just that, i want to actually focus on the problem.

#ok, I think this is insanely helpful already. 
from binarytree import bst;

# I think I have the correct algorithm
# maybe? I am not certain. 
def findSecondLargest(Tree):
   currNode = Tree;
   parentNode = Tree;
   while currNode.right != None:
        parentNode = currNode
        currNode = currNode.right
   #     
   return parentNode.value
   # if parentNode.left != None: 
        # return parentNode.left.value
   # else: 
        # return parentNode.value
   
   

if __name__ == "__main__":
    Tree = bst(height=3, is_perfect=False)
    print(Tree)
    print(findSecondLargest(Tree))