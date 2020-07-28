# Given an array of integers, find the first missing positive integer in linear time 
# and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def HashTableMethod(listC):
# this method uses O(n) time, and uses O(n) memory.
    hashtable = {}
    for item in listC:
        if item < len(listC) and item > 0: # as a small realization this line doesnt need to exist, but it can techinically speed up, calculations. 
            hashtable[item]  = True
    missingPostive = 1
    while missingPostive in hashtable:
        missingPostive += 1
    return missingPostive
    
# a chance in the future rewrite code to use this method
# from https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

        
listC = [3, 4, -1, 1]
print(listC)
print("the missing value is",HashTableMethod(listC))
listC = [1, 2, 0]
print(listC)
print("the missing value is",HashTableMethod(listC))