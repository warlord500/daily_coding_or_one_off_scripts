#!/bin/python
#given an array of integers. 




#this algorithm works by effectively sorting the data into one of two sections.
# however in practice their is a middle section called search section. 
# duplicate section contains all elements that have duplicates including the duplicates next to each other.
#the unique section contains all the unique integers. 

# dammn there has got to be a faster way to do this?
# at least this alogthirim, uses constant space. 
# however it alters info in the array. 
def findIntegers(list):
    uniqueIndex=0
    duplicateIndex = len(list) - 1
    #
    # run search passes
    # the maximum number of search passes this can run is length  of list.
    # however the maximum number of comparisons is (n)(n+1)/2. 
    # which only occurs when all items in the list are unique. 
    # average performance should be n(n+2)/4
    while uniqueIndex + 1 < duplicateIndex:
        # time to search for a specific element.
         currentElem = list[uniqueIndex];
         searchIndex=uniqueIndex;
         isUnique=True
         while searchIndex <= duplicateIndex:
         # ok found duplicate.
                if currentElem == list[searchIndex]:
                      # swap current element to duplicate section.
                      list[searchIndex], list[duplicateIndex] = list[duplicateIndex], list[searchIndex]
                        duplicateIndex -= 1; # grow the duplicate section. 
                        if isUnique:
                            isUnique = False
                            list[uniqueIndex], list[duplicateIndex] = list[duplicateIndex], list[uniqueIndex]
                            duplicateIndex -= 1; # grow the duplicate section. 
                            
                searchIndex += 1
        # no duplicates were found. 
        if isUnique: 
            uniqueIndex += 1
    return list[0:uniqueIndex-1]    
                        
    
   

if __name__ == "__main__":
    print(function())