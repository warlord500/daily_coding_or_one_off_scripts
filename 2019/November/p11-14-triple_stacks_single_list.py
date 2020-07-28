#!/bin/python


#implement 3 stacks using a single list:
#ok I got two ideas allocate  a large list and segerate 
#each stack. 
#other option is to use flags with items.
class SegeratedStack:
    def __init__(self,maxSize):
        self.list = [] * (maxSize*3)
        self.stacks = [3,maxSize,maxSize*2]
        self.stackSize

    def pop(self, stack_number):
        if self.itemsInStack(stack_number) >= 1:
             self.list[self.stacks[stack_number]] = Null;
             self.stacks[stack_number] -= 1;
        else:
            raise("error no items in stack");

    def push(self, item, stack_number):
        if self.maxItemsToFill(stack_number) > 0:
            self.list[self.stacks[stack_number]] = item;
            self.stacks[stack_number] += 1;
        else:   
            raise("error no space in stack!!");
        
    def itemsInStack(self,stack_number):
        return  self.stacks[stack_number] - (self.stackSize*(stack_number))
        
    def MaxItemsToFill(self,stack_number):
        return self.Stacksize - self.itemsInStack(stack_number);

def function():
   return "hello world"

if __name__ == "__main__":
    print(function())