# i am skipping this today so that, i can work on homework. maybe one day i will finish it!

#https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
#code stolen from 
#https://stackabuse.com/stacks-and-queues-in-python/
import time
class jobScheduler():
    def __init__(self):
     self.queue = []
    
    def addItemToRun(self,function,msToRun):
        absoluteMs = msToRun + int(round(time.time() * 1000))
        if len(self.queue) == 0:
            self.queue.append((function,absoluteMs))
            return None
        else: 
           i = 0
           while i < len(self.queue):
                if self.queue[i][1] >  absoluteMs:
                    self.queue.insert(i,(function,absoluteMs))
                    return None
                i += 1
           self.queue.append((function,absoluteMs)) # at this point we are sure that there is no jobs that run before us just put it in the back!
           return None
           
    def printQueue(self):
        print(self.queue)
    
    def runLoopOnce(self): #this runs jobScheduler Once
         currentTime = int(round(time.time() * 1000));
         if self.queue[0][1] >=  currentTime;
            self.queue[0][0]()
            self.queue.pop(0)
            return 0
        else:
            # return the difference for cases like sleep function
            return self.queue[0][1] - currentTime
            
    def runLoop(self):
            while self.queue:
                sleepFor = self.runLoopOnce()
                #time.sleep(sleepFor) # not 100 precent aware if this is the best way to write this. 
                
def printSomeCode():
    print("printing some code")
def task_2():
    print("task 2")
def task_3():
    print("task tri")
def task_4
    print("task 4")
jobs = jobScheduler()
jobs.addItemToRun(printSomeCode,95)
jobs.addItemToRun(task_2,100)
jobs.addItemToRun(task_3,92)
jobs.addItemToRun(task_4,90)

jobs.printQueue()
jobs.runLoop()