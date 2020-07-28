
class FileNode:
    def __init__(self,name):
      self.name = name.lstrip("\t")
      self.subDirectories = []
      self.files = []

def generateTreeOfFiles(string):
      listOFFileNodes = string.split("\n");
      numOfFileNodes = len(listOFFileNodes)
      Tree = FileNode(listOFFileNodes[0])
      stackOfSubDirs = [Tree]
      if numOfFileNodes <= 1:
            return Tree
      else:
        index = 1; # first node!
        while index < numOfFileNodes:
            newLevel = count_char(listOFFileNodes[index],"\t");
            print(newLevel)
            if  not newLevel == len(stackOfSubDirs):
                while len(stackOfSubDirs) > newLevel:
                    stackOfSubDirs.pop()
                    
            if "."  in listOFFileNodes[index]: # if is normal file!
                stackOfSubDirs[-1].files.append(FileNode(listOFFileNodes[index]))
            else:
                print(stackOfSubDirs[-1])
                stackOfSubDirs[-1].subDirectories.append(FileNode(listOFFileNodes[index]))
                stackOfSubDirs.append(FileNode(listOFFileNodes[index]))
        
            index += 1
      return Tree
      
 

def count_char(string= '', char='', start=True):
    count = 0
    if not start:
        string = string[::-1]

    for k in string:
        if k is char:
            count += 1
        else:
            break
    return count
    
#this is the actually important part of the code!
#going to use recursion here rather than try to emulate using 
#iteration which would be a lot harder to understand!
def getMaxPath(Tree,prefixA=0):
    prefixLength = prefixA + len(Tree.name)
    maxPathLength = prefixLength;
    for item in Tree.files:
        maxPathLength = max(prefixLength + len(item.name),maxPathLength)
    #this part uses recursion 
    #any can additionally every item could  be ran concurrently
    for item in Tree.subDirectories:
         maxPathLength = max(getMaxPath(item,prefixLength),maxPathLength)
    return maxPathLength
    
    

data= "code\n\ttest.txt\n\tnext.txt\n\tthisCodeIsverylong\n\t\ttest"
print(getMaxPath(generateTreeOfFiles(data)))