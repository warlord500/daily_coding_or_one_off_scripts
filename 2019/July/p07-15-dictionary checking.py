# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# # Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']


#ok performance, i beleive this operates as O(n) 
# it has memory performance of O(n) n being length of string. 
# it does have one major flaw 
# it could be turned to some sort of iteration object that uses very little memory 
# and returns slices too! 
# making this code perform fairly well! 

def findWordsList(string,dict):
      listOfCurrentWords = []
      startOfCurrentWord = 0
      while startOfCurrentWord < len(string):
        lengthOfCurrentWord = 1;
        while True : # ok this seriously akward but i dont know a better way to write it as of know. 
                if startOfCurrentWord + lengthOfCurrentWord > len(string):
                    return None
                else:
                    attempt = string[startOfCurrentWord:  startOfCurrentWord +lengthOfCurrentWord]
                    if attempt  in dict:
                        listOfCurrentWords.append(attempt)
                        startOfCurrentWord += lengthOfCurrentWord
                        break
                lengthOfCurrentWord += 1
      return listOfCurrentWords
        #ok what to write here? 
        #i guess we could use a really simple hash set? 
        #in fact it doesnt matter what the structure is because we just need to check i
        
dict = set(["bed","bath","and","beyond","quick","brown","the","fox"]);


string = "bedbathandbeyond"
print(findWordsList(string,dict)) # works
string2 = "bedbathandbeyonds" 
print(findWordsList(string2,dict))
string3 = "thequickbrownfox"
print(findWordsList(string3,dict))