#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?
def anyTwoToK(listC,k):
    if len(listC) < 2:
        return listC[0] == k 
    else:
        i = 0
        j = 1
        while i < len(listC):
            if listC[i] + listC[j] == k:
                return True
            j += 1
            if j == len(listC):
                j = 0
                i += 1
        return False
    
print(anyTwoToK([10,2],12))     # false
print(anyTwoToK([10,3],12))     # false
print(anyTwoToK([10,3,4],12))   # false
print(anyTwoToK([10],12))       # false
print(anyTwoToK([6,2,10,6],12)) # true

