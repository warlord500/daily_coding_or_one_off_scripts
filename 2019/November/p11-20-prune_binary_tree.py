#!/bin/python
# Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

# For example, given the following tree:

   # 0
  # / \
 # 1   0
    # / \
   # 1   0
  # / \
 # 0   0

# should be pruned to:

   # 0
  # / \
 # 1   0
    # /
   # 1
 
 # 1
    # \
     # 0
    # / \
   # 0   0 
# We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

def prune_binary_tree():
# ok start from the bottom and work your way up
# is there a way to associate more data to each node?
# like a true false value?
# in the top case I really dont think it would matter.
# I guess it might not be 


# ok better idea. 
# repeatly delete leaf nodes that are 0.
# until you cant delete leaf nodes anymore at which point you have removed all just 0 containing subtrees.
    leafNodes = getLeafNode(tree);
    while leafNodes:
        for leaf in LeafNodes:
           parent =  getParentOfLeafNode(leaf);
           if determineLeafNodeRight():
                parent.right = null;
           else: 
                parent.left = null;
        
        
def prune_binary_tree_rec(node):
    if node.left != null and prune_binary_tree_rec(node.left):
        node.left = null;
   
    if node.right != null and prune_binary_tree_rec(node.right):
        node.right = null;
    return  node.value == 0 and node.left == null and node.right == null;
       

if __name__ == "__main__":
    print(function())