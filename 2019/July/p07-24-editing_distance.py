#!/bin/python


# a really good resource: 
# https://medium.com/@dakota.lillie/an-intro-to-dynamic-programming-pt-ii-edit-distance-ceed0b12fe6d



# this is a really naive solution. 
# that actually doesnt work for all problems.
# due to the fact if you have to insert in the beginning or middle 
# for minimum this will attempt extraneous replaces or delets
def minimum_editing_distance(src,dest):
    #if one is bigger, delete or append the items to end!
    editing_distance = abs(len(src) - len(dest));
    currPos = 0;
    lengthToRun = min(len(src),len(dest));
    while currPos < lengthToRun:
        if src[currPos] != dest[currPos]:
            editing_distance += 1
        currPos += 1
    
    return editing_distance
    
    
    


if __name__ == "__main__":
    print(minimum_editing_distance("cat","hat")) # 1
    print(minimum_editing_distance("sand","sandwich")) # 5
    print(minimum_editing_distance("hat","shit")) #  2 gives 4
    