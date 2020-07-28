#!/bin/python
#this is a recursive function 
def expressionTreeEvaluate(root):
   if root.leaf: 
        return root.value
   else: 
        leftSide = expressionTreeEvaluate(root.left);
        # the right side can be done cocurrently with respect to left side calculation
        rightSide = expressionTreeEvaluate(root.right);
        if root.value = "*":
            return leftSide*rightSide
        if root.value = "+":
            return leftSide+rightSide
        if root.value = "/":
            return leftSide/rightSide
        if root.value = "-":
            return leftSide-rightSide
         

if __name__ == "__main__":
    print(function())