# For example, given the following Node class

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


# how should i serialize something like this? 
# something looking like json library? that could work

    
    
class Node:
   def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    
   def serialize(self): # serililize the data base on json
        string = "{ val: \"" + self.val + "\","
        left =  "left:" + self.left.serialize() + "," if self.left != None else ""
        right = "right:" + self.right.serialize() + ","  if self.right != None else ""
        return  string + left + right + "}" 
   def deserialize(string):
            return None; # i am not sure where to start with this? 
   
       
print(Node("test",Node("code"),Node("right")).serialize())
       
