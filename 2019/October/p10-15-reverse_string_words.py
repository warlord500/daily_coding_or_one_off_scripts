#!/bin/python

# Given a string of words delimited by spaces, reverse the words in string. 
# For example, given "hello world here", return "here world hello"

# Follow-up: given a mutable string representation, can you perform this operation in-place?
def reverseWordsInString(string):
   listOfIndexWords = getIndexForWords(string)
   # how do you do this in-place without 
   # making a fullcopy of each word?
   #you would have to use insertion which would be slower than this method. 
   stringToBuild = ""
   currentIndex = len(listOfIndexWords) - 1
   while currentIndex > -1: 
            startOfWord = listOfIndexWords[currrentIndex].0
            endOfWord =  listOfIndexWords[currrentIndex].1 
            stringToBuild += string[startOfWord:endOfWord]
    return stringToBuild


def getIndexForWords(string):
    listOfIndexes = []
    startOfWord = 0
    print("varible init") # skip thru white space in the front of the string
    while startOfWord < len(string):
         if  string[startOfWord] == ' ':
             startOfWord += 1
    currentEnd = startOfWord
    while currentEnd < len(string):
            print(currentEnd)
            if string[currentEnd] == ' ':
                listOfIndexes.append((startOfWord, currentEnd))
                while currentEnd < len(string):
                     if  string[currentEnd] == ' ':
                        currentEnd += 1
                     else:
                        break;
                startOfWord = currentEnd
            else:
                currentEnd += 1
    if string[currentEnd] != ' ':
        listOfIndexes.append((startOfWord, currentEnd))
    return listOfIndexes
    
    
if __name__ == "__main__":
    print("hello world here")
    print(getIndexForWords("hello world here"))
    print(getIndexForWords("here world hello"))