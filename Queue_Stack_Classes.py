#QUEUE CLASS 
#head points to the last in (end of queue) and tail points to first in (first to get in first to get out)
from LinkedList import LinkedList
from Node import Node
from scifi_LNode import scifi_LNode


class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        
    def enqueue(self, what):
        super().goBeginning()
        super().InsertBefore(what)
        
    def dequeue (self):
        super().goEnd()
        x = super().getData()
        super().remove()
        return x
    
    def peek(self):
        super().goBeginning()
        x = super().getData()
        return x
    
class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        
    def push(self, what):
        super().append(what)
        
    def pop(self):
        super().goEnd()
        x = super().getData()
        super().remove()
        return x
    
    def peek(self):
        super().goEnd()
        x = super().getData()
        return x

class priorityQueue(Queue):
    def __init__(self):
        super().__init__()
    def insertPQ(self,what,priority):
        #inserts a node according to priority
        node = scifi_LNode(what, priority)
        super().goBeginning()
        #for when you are starting PQ
        if super().isEmpty() == True:
            super().insertBefore(node)
            return
        
        #go through and find right position when queue is longer than 1 element
        while super().isEnd() == False:
            currPriority = super().getCurr().priority
            if currPriority < priority:
                #insert before here
                super().insertBefore(node)
                return
                #break #we do not need to continue going through the list if the current priority is greater than new priority so we should insert before
            super().goNext()
        
        
        
        #for when PQ is one item element or when you have gotten to the last element and still have a smaller priority
        if super().isEnd() == True:        #check last position bc while statement does not do that
            currPriority = super().getCurr().priority
            if currPriority < priority: #new node should go right before last one
                    super().insertBefore(node)
            else: #new node should be the last element
                super().append(node)
        return
                    

            
            
  
