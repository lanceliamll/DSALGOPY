
# Stack & Queues
# last in first out FIFO
# Push, Pop & Peek
# Push to the array
# Pop the last added data
# Peek the last added data


class Stack(object):
    def __init__(self):
        self.stack = []
        
    #Push always on the first position of the array
    def push(self, data):
        self.stack.append(data)
    
    #Pop out of the Array, Pop the last in data
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #Peek the last or the latest pushed data on the array
    def peek(self):
        data = self.stack[-1]
        return data
    
    def printData(self):
        for data in list(self.stack):
            print(data)
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()

stack.printData()
print("Peek", stack.peek())
    
    
    
    