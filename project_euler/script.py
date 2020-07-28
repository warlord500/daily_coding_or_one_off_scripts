#!/usr/bin/python
num =600851475143

primes={3,5,7,11,13,17,19,23,29,37,39}
for pnum in primes:
   result=num%pnum;
   if result == 0:
       break;
print pnum,", ",result;
