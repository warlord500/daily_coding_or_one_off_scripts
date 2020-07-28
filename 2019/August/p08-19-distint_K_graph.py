#!/bin/python
# Given an undirected graph represented as an adjacency matrix and an integer k, 
# write a function to determine whether each vertex in the graph can be colored such that no two 
# adjacent vertices share the same color using at most k colors.


# this algorithm takes O(n^2) time and O(n) space. 
# I don't know if there is a faster way to do this.
# this has one problem. 
# if any part of node structure floats or 
# node cant reach any other node via edges 
# then this will give wrong answer!
# to check for that you would have to use a factorial problem solver. 
def checkGraphWithKDistinctColors(graph,k,NumberOfNodes):
    #check for easy case should always work!
    if k >= NumberOfNodes:
        return True;
    else:
        countOfAdjacentNodes = [0]*NumberOfNodes;
        # ok, I think the idea is to figure out the maximum,
        # number of adjacent nodes and then check if that is lower than k.
        n = 0
        while n < NumberOfNodes:
            index = n; # skip double edges, in the case of directed.
            # you have to set index to 0 each time.
            while index <  NumberOfNodes:
                if graph[n][index]: # we have an edge from n to index.
                   countOfAdjacentNodes[index] += 1;
            n += 1
        minimumK = max(countOfAdjacentNodes);
        # special case scenario of all nodes are connected to each other.
        # which means everything needs to up 1.
        if minimumK = NumberOfNodes-1:
            minimumK += 1
        return minimumK;
       

if __name__ == "__main__":
    print(function())