#!/bin/python
import random
# You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

# You can generate random numbers between 0 and 1 uniformly.
def chooseATRandom(choices,probabilities):
# assert that the probabilities do actually add up to 1.0 or 
# rather close to one. 
    assert(sum(probabilities) == 1.0); # 
    assert(len(probabilities) == len(choices));
    pureRNG = random.random();
    startOfRegion = 0.0
    endRegion = 0.0;
    currentIndex = 0;
    for i in probabilities:
        endRegion = startOfRegion + i;
        if pureRNG > startOfRegion and  pureRNG < endRegion:
            return choices[currentIndex];
        startOfRegion = endRegion;
        currentIndex += 1
        
    raise("this shouldnt possible");
    #pseudo code.
# regions based on probalities.
# for example two's region is from (0.1,0.6)
# however 0.1 exclusive. 
#

if __name__ == "__main__":
    choices = [1, 2, 3, 4];
    probabilities = [0.1, 0.5, 0.2, 0.2]
    for _ in range(0,10):
        print(chooseATRandom(choices,probabilities))