#!/bin/python

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. 
#For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
#You can assume the string to be decoded is valid.


#small note to myself this could be better if you used full dictionary method
#however because we aren't doing that its going to be relatively simple.
from io import StringIO
def runLengthEncode(uncompressed):

   if len(uncompressed) == 0:
        return ""
   lastCharToEncode=uncompressed[0];
   currentPosition=0;
   lengthOfRun=1;
   encodedString= StringIO()
   while currentPosition + lengthOfRun < len(uncompressed):
           if uncompressed[currentPosition + lengthOfRun] == lastCharToEncode:
                lengthOfRun += 1;
           else:
                if lengthOfRun > 1:
                    encodedString.write(str(lengthOfRun))
                encodedString.write(lastCharToEncode)
                currentPosition += lengthOfRun
                lengthOfRun = 1
                lastCharToEncode = uncompressed[currentPosition:currentPosition + 1];
    
   return encodedString.getvalue()
                       

if __name__ == "__main__":
    print(runLengthEncode("AAAABBBCCDAA"))