# intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are size of lists) and O(1) space

#ok first attempt
#naive i know but i have to write something!!
# this works in O(n * m) time but in O(1) space
def searchLists(first,second):
    currentFirst= first.head;
    currentSecond = second.head;
    while currentFirst: 
        while currentSecond: 
            if currentSecond == currentFirst:
                return currentSecond.item
            currentSecond = currentSecond.next;
            
        currentFirst = currentFirst.next;
        currentSecond = second.head
    return None;

# i had an idea of finding the last matching Node
# if this was a doubly linked list by working backwards and checking for the last 
#known match. 
#in theory this acheives O(S) 
# where s is shared length between the two.
# but this takes O(m + n) space due to being singly linked!
def searchListsFast(first,second):
    return None
    
#I have an idea for a solution 
# i think this will work! 
# it will achieve O(max(M,N)) time, 
# and O(1) space which is even better than the proposed solution above. 
# however this has one problem it requires knowing the length of the lists.
# which means that shared cant be altered 
# or you reduce the solution to something like M + N for length
# then min(M,n) actual comparing, plus Max(m,n)-min(m,n) simplified to Max(M,n) run.
# maybe not as fast as i want! 
# so in the end what you get is O(M + N + max(m,n)) and O(1). unoptimized unknown list size.
def solution(first,second):
    currentFirst = first.head;
    currentSecond = second.head;
    if first.length  > second.length:
        currentFirst = skipNodes(currentFirst,first.length - second.length);
    if second.length > first.length: 
        currentSecond = skipNodes(currentSecond,second.length -  first.length);
    #main code - current pointers now have equal number of nodes in length!
    #also guaranteed to have same node at same distance from beginning  
    while currentFirst and currentSecond:
       if currentFirst == currentSecond:
           return currentFirst.item
       currentFirst = currentFirst.next
       currentSecond = currentSecond.next
    return None #dont share any nodes!


#sub function shared between to if code!
def skipNodes(pointer,numOfNodes):
    while numOfNodes > 0:
        pointer = pointer.next
        numOfNodes -= 1
    return pointer
        
    
    
class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
        
    def addItemTOList(self,item):
        newNode = Node(item,self.head);
        self.head = newNode; 
        self.length += 1
        
    def addEntireListToEnd(self,list):
        self.length += list.length
        if not self.head:
            self.head = list.head;
        else:
            currentNode = self.head
            while currentNode.next: # find the end of list!
                currentNode = currentNode.next
            #found the end of list now time to add it 
            currentNode.next = list.head
        return None
        
        
    def printList(self):
        print("[{ ", end="")
        currentNode = self.head;
        while currentNode:
            print(currentNode.item, end="")
            print(", ",end="")
            currentNode = currentNode.next
        print(" }]\n", end="", flush=True)
        

list = linkedList();
list.addItemTOList(1)
list.addItemTOList(2)
list.printList()
sec = linkedList()
sec.addItemTOList(4)
sec.addItemTOList(5)
sec.printList()
sec.addEntireListToEnd(list)
sec.printList()
third = linkedList()
third.addItemTOList(6)
third.addItemTOList(7)
third.addEntireListToEnd(list)
third.printList()
print(searchLists(sec,third));
print(solution(sec,third));