#!/bin/python
import random;
# Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

#You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
def sumWithRangeIndex(listOfNumbers,i,j):
    # validate arguments with asserts.
    assert(i < len(listOfNumbers));
    assert(j <= len(listOfNumbers));
    assert(i < j);
    assert(i >= 0);
    assert(j >= 0);
    total = 0;
    currentIndex = i
    while currentIndex < j-1:
        total += listOfNumbers[currentIndex];
        currentIndex += 1;
    return total;
    
def standardSum(listOfNumbers):
    total = 0;
    currentIndex = 0;
    while currentIndex < len(listOfNumbers):
        total += listOfNumbers[currentIndex];
        currentIndex += 1;
    return total;

if __name__ == "__main__":
    for item in range(10):
        list = []
        for item in range(10):
            list.append(random.randrange(10));
        startIndex = random.randrange(0,5);
        endIndex = random.randrange(5,10);
        print("startIndex: ", startIndex,"end Index: ", endIndex);
        print("the list: ", list);
        print("sumWithRange: ", sumWithRangeIndex(list,startIndex,endIndex));
        print("sum with subList", sum(list[startIndex:endIndex-1]));
