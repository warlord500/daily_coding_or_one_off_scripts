#!/bin/python
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.

# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
# I swear I have done this before!! 
# but with  something else? like a finding words who are the same backwards and forwards!
# for finding palindromes
def contiousSum(list,sumTarget):
   pos = 0
   size = len(list)
   while size > 0:
        pos = 0
        while pos + size <= len(list): 
            if sum(list[pos:pos+size]) == sumTarget:
                return list[pos:pos+size]
            pos += 1
        size -= 1

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    print(contiousSum(list,9))
    list = [1, 2, 3, 4, 5]
    print(contiousSum(list,6))
    list = [1, 2, 3, 4, 5]
    print(contiousSum(list,7))
    