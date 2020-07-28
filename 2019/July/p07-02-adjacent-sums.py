# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
# Numbers can be 0 or negative.\
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# i dont know the actual solutions to this problem, but i wonder if i could at least get the 
#answer to how many possible combinations are there for adjacent numbers in a list. 
# and then could you filter them down to n amount?


#instead of finding the largest sum
# my first goal is there a way to find the number of possibilites?
#and maybe check sections of possibilites to remove themm? 
# i dont think possiblities grow linerally with ever len of list increasing?
def findMaxSumOfNonAdjacentNums(listN):
    lenN = len(listN)
    if lenN == 1:
        return listN[0]
    elif lenN == 2:
        return max(listN[0],listN[0])
    else:
        incl = listN[0]
        excl = 0;
        currIndex = 0
        while currIndex < lenN:
            excl_new = max(excl,incl)
            incl = listN[currIndex] + excl
            excl = excl_new
            currIndex += 1
        return max(incl,excl)
     
# ok, number possibilites for 4 are 3
#5 = 6 
#6 = 
test1 = [-1,2,5,-3,-1,7,4,2,3,1]
print("test1:",findMaxSumOfNonAdjacentNums(test1)," should be 15")
test2 = [-1,2,5,-3,-1,7]
print(test2)
print(        