#!/bin/python
# Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
def closestToPoint(point,k,list):
    closeItems = [];
    
    for point in list:
        currDistance = distance(point,item);
            if currDistance < list[-1]:
                spot= k-1;
                for items in list.rev(): # not sure if this is actual code in python
                    if currDistance > items.1:
                        list.insert(spot,(point,distance));
                        # but it is gonna have to work for know.
                        # the insertion logic is gonna have be reworked tommorow
                list.pop() # too many items in list!
   return "hello world"
   
def distance(point1,point2):
    # this pretty close to the algothirim.
    return Math.sqrt(pow(point1.0 - point2.0,2) + pow(point1.1-point2.1,2));

if __name__ == "__main__":
    print(function())