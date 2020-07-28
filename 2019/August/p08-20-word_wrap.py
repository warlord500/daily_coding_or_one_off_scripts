#!/bin/python
# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. 
# You must break it up so that words don't break across lines. 
# Each line has to have the maximum possible amount of words. 
# If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and 
# that there is exactly one space between each word.

# For example, 
# given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
# you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
# No string in the list has a length of more than 10.

def breakUpStringOfText(string,k):
   endOfLastString = 0;
   currentChar = 0;
   lengthOfList = len(string);
   listOfLines = [];
   while currentChar < len(string):
        if currentChar - endOfLastString > k:
            #stop counting and create substring
            # check if impossible to break up!
            listOfLines.push(string[endOfLastString:indexOfLastWordChar]);
            endOfLastString = indexOfLastWordChar;
        else currentChar = " ":
            indexOfLastWordChar = currentChar;
    currentChar += 1;
    
    
if __name__ == "__main__":
    print(function())