#!/bin/python

#probably not the fastest method there is. 
# effectively takes o(n) time but
# takes three comparisons every number. 
# and has to deal with an inefficient insertion method.
def max_product(num_list):
    if len(num_list) < 3:
        return 0;
    else:
        listMaxes = [0] * 3;
        for i in num_list:
            j = 0;
            while j  < 3: 
                if abs(i) > abs(listMaxes[j]):
                    listMaxes.insert(i,j); insert new item at location
                    listMaxes.pop(); remove last extraneous
                    break;
                j += 1
        return product(listMaxes);
                
   

if __name__ == "__main__":
    print(function())