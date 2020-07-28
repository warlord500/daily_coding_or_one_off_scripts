#Given an array of integers, return a new array such that each element at
#index i of the new array is the product of all the numbers in
#the original array except the one at i.
#import numpy
def getProductWithDiv(listc):
     result = 1
     retList = []
     for i in listc:
         result *= i
     for i in listc:
         retList.append(result/i)
     return retList

def getProductWODiv(listc):
     skipvalue = 0
     retList = [1] * len(listc)
     while skipvalue < len(listc):
         i = 0
         while i < len(listc):
             retList[skipvalue] *= listc[i] if i != skipvalue else 1
             i += 1
         skipvalue += 1
     return retList
        
# this is division but it only works with whole numbers.
# it can work with fractional amounts but only returns full divisions and remainders

def emulateDivision(num,divisor):
    count = 0;
    postive 1 if (is_postive(num) ^ is_pos(divisor)) else -1 # this confusing line of code says if 
    num = abs(num)
    divisor = abs(divisor)
    while num > 0: 
        num -= divisor
        count += 1
    return (count-1)*positive


    
print(getProductWithDiv([2,7,3])) # [21,6,14] 
print(getProductWODiv([2,7,3]))
print(getProductWithDiv([1,2,3,4,5]))
print(getProductWithDiv([3,2,1]))
