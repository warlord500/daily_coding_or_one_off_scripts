# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
#For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# learing higher order programming in python.
#first attempt of accessing closure elements didnt work.
# but using pair function actually implemantion to return correct item did work!!!
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def returnFirst(a,b):
        return a
    return pair(returnFirst)

    
def cdr(pair):
    def returnSec(a,b):
        return b
    return pair(returnSec)


# Implement car and cdr
print(car(cdr(cons("code",cons("maybe","not"))))) # should return "maybe"


