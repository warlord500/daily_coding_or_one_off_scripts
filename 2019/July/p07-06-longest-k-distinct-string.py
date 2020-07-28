# Given an integer k and a string s, 
# find the length of the longest substring that contains at most k distinct characters.
# my algorithm isn't very fast
# it checks every possibility but if it finds a maximum one it stops. 
# For example, given s = "abcba" and k = 2, 
# the longest substring with k distinct characters is "bcb".

#this methods preforms at 
# O((n-k)^2)and has memory requirements of 
# O(n) if using copies or
# O(k) if using slices
def findSubString(listC,k):
        lengthOfList = len(listC)
        if lengthOfList == 0:
            return []
        elif lengthOfList <= k:
           return listC
        else:
          sizeOfSlice = lengthOfList
          while sizeOfSlice > k:
            startOfSlice = 0
            while startOfSlice + sizeOfSlice <=   lengthOfList:
                   slice = listC[startOfSlice:startOfSlice + sizeOfSlice]; # this is absolutely horrible performance
                   # because copies a good chunk of the original list with while loop. 
                   # rust can do this better simply because it doesn't need to copy every time!
                   if checkContainsOnlyKdist(slice,k):
                        return slice
                   startOfSlice += 1
            sizeOfSlice -= 1
        #this minor optimization just stops doing checking because 
        #the first slice of the list is the biggest you can get with k distinct letters
        return listC[:sizeOfSlice] 
        
        
        
def checkContainsOnlyKdist(slice,k):
    distinctLetters = set()         
    currIndex = 0
    sliceLength =  len(slice)
    while currIndex < sliceLength and len(distinctLetters) <= k:
        if  not (slice[currIndex] in distinctLetters):
            distinctLetters.add(slice[currIndex])
        currIndex += 1
    return len(distinctLetters) <= k
    
# print(checkContainsOnlyKdist("abc",3))
# print(checkContainsOnlyKdist("abcc",3))
# print(checkContainsOnlyKdist("abbc",3))
# print(checkContainsOnlyKdist("abbc",3))
# print(checkContainsOnlyKdist("not true",3))
# print(checkContainsOnlyKdist("sandwich",8))    
print(findSubString("sandwhichhich",7))
print(findSubString("abcba",2))