#!/bin/python
# Given an even number (greater than 2), return two primes numbers whose sum will be equal to the given number.

# A solution will always exist. See Goldbach’s conjecture.

# Example:

# Input: 4
# Output: 2 + 2 = 4

# If there are more than one solution possible, return the lexicographically smaller solution.

# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

# [a, b] < [c, d]

# If a < c OR a==c AND b < d.

#the fastest algorithm I can think of is straight up brute
#force it will take O(n^2) time. n being the number of items below 
# number to be the sum.

import random;
def pairOfPrimeForEven(num):
    primes = [2, 3, 5, 7, 11, 13, 17,19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,83, 89, 97, 101]
    pL = len(primes)
    base = 0;
    while base < pL:
        adder = 0
        while adder < pL:
            if primes[base] + primes[adder] == num:
                print("iterations ran:", base + adder);
                print("value trying to reach:", num);
                return (primes[base], primes[adder])
            adder += 1;
        base += 1
        
if __name__ == "__main__":
    print(pairOfPrimeForEven(4))
    for _ in range(0,10): # quick random test for checking this works with alot numbers.
       randEven = random.randint(2,50)*2;
       print(pairOfPrimeForEven(randEven))
       print("\n\n");