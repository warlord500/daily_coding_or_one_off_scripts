#!/bin/python
# This problem was asked by Google.

# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

# small note this is more pesudo code than anything else.
def isDoubleLinkedAPalindrome(list):
    # the step code could be gotten rid of 
    # then you would have to detect that firstHalf and SecondHalf 
    # are not Null.
    # though in those I dont do null checking because I assume that every single 
    # link beside the last are null. and you dont need to go that far. 
    maxStepsNeeded = len(list)/2
    currentSteps = 0
    firstHalf = list.head
    secondHalf = list.tail
    while currentSteps < maxStepsNeeded
        if firstHalf.value != secondHalf.value:
            return False
        currentSteps += 1
        firstHalf = firstHalf.next
        secondHalf = secondHalf.prev
    return True # we didnt dectect non symmetry

if __name__ == "__main__":
    print(function())