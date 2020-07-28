
#cheating with max function which makes 
#getting the max of some array to be easy.
# assuming max uses O(n) time and O(1) space. 
# this uses O(n) time and O(n/k) space 
def maxSubArray(ListC,k)
    maxes = []
    currIndex = 0
    if k >= ListC: # error bad input! 
        return None
    while k + currIndex < len(ListC):
        maxes.append(max(listC[currIndex:currIndex + k]))
        currIndex += 1
    return maxes;
    
list = [10,8,