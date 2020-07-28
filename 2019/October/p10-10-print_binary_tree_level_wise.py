#!/bin/python
#this is yesterdays problem!!

# Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  # 1
 # / \
# 2   3
   # / \
  # 4   5

from binarytree import bst;

# ok here is a quick question how do you do this with out using huge amounts 
# memory?
# o(n^2) is the algothirimic speed.
def printBinaryTreeLevelWise(Tree):
   currentLevel = 0; # 0 is root and number bigger is closer to the leaves
   maxLevel = Tree.height
   while currentLevel <= maxLevel: 
        subPrintBinaryTree(Tree,currentLevel,0)
        currentLevel += 1

def subPrintBinaryTree(Node,levelToProcess,currentLevel):
    if levelToProcess == currentLevel:
        if hasattr(Node,'value'):
            print(Node.value, ", ")
    else:
        subPrintBinaryTree(Node.left,levelToProcess,currentLevel+1)
        subPrintBinaryTree(Node.right,levelToProcess,currentLevel+1)
        
        # do nothing 


if __name__ == "__main__":
  Tree = bst(height=4, is_perfect=True)
  print(printBinaryTreeLevelWise(Tree))
  print(Tree)