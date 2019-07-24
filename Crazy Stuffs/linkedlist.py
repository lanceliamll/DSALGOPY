


class Node(object):
    def __init__ (self, data):
        self.data = data
        self.nextNode = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
     #Speed O(1)   
    def insertFirst(self, data):
        
        #Increase the size
        self.size += 1
        
        #Initialize the new Node
        newNode = Node(data)
        
        #if no current head
        if not self.head:
            self.head = newNode
        else:
            #if meron nang node, then yung bagong node is may next node, ayun sya
            newNode.nextNode = self.head
            #assign the newNode to be the head node
            self.head = newNode
        
        
    #Speed O(N)
    def insertLast(self, data):
        
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode
        
        
    #remove
    def remove(self, data):
        
        #Means walang data
        if self.head is None:
            return
        
        self.size -= 1
        currentNode = self.head
        previousNode = None
        
        while currentNode.data != data:
            #Loop Through the array/list if the data is not equal to the data inserted
            #To be find
            previousNode = currentNode
            currentNode = currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
            
        
            
        
    def linkedSize(self):
        return self.size
        


    #Traverse List or PrintList
    def traverseList(self):
        
        actualNode = self.head
        
        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode
        
        

ll = LinkedList()

ll.insertFirst(10)
ll.insertFirst(12)
ll.insertLast(133)
ll.remove(133)




ll.traverseList()

print("The size of the linkedList:", ll.linkedSize())
