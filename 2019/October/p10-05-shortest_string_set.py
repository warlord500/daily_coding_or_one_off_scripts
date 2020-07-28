#!/bin/python
# Given a string and a set of characters, return the shortest substring containing all the characters in the set.

# For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

# If there is no substring containing all the characters in the set, return null.
def find_smallest_substring_with_set(string,set):
    pos=0 
    size=len(set) # set up to at least as big as set
    while size < len(string):
        pos = 0
        while pos + size <= len(string):
            print("pos: ", pos, "size: ", size);  
            if checkForCharactersInSet(string[pos:pos+size],set):
                print("pos: ", pos, "size: ", size, " -- completeled");  
                return string[pos:pos+size]
            pos += 1
        size += 1

def checkForCharactersInSet(string,set):
    pos = 0;
    charInSet = dict();
    for k in set:
        charInSet[k] = False
    while pos < len(string):
        if string[pos] in charInSet:
            charInSet[string[pos]] = True
        pos += 1
            
    allTrue = True
    for k, v in charInSet.items():
        allTrue &= v
    
    return allTrue;
    
if __name__ == "__main__":
    string = "figehaeci"
    set = {"a", "e", "i"}
    print(find_smallest_substring_with_set(string,set))