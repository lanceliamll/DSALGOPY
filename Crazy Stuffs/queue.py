

#Queues

# FIFO - First in First Out 

#Enqueue - Insert to the array 
#Kapag nalalagay tayo ng data, dapat papuntang last always
# or the end of the array

#Dequeue = Remove from the array
#Kapag nag dedequeue remove yung first na nilagay natin.


class Queues(object):
  def __init__(self):
    self.stack = []

  #Laging add sa hulihan ng array
  def enqueue(self, data):
      self.stack.append(data)

  #Laging remove yung hulihan sa rray
  def dequeue(self):
    data = self.stack[0]
    del self.stack[0]
    return data

  #Peek kunin yung ininsert na una so yung last na array
  def peek(self):
    data = self.stack[0]
    return data


  def printData(self):
    # for item in list(self.stack):
    #   print(item)
    print(self.stack)


q = Queues()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("DEQEUED", q.dequeue())
print("DEQEUED", q.dequeue())


print("Peek the first:", q.peek())
q.printData()


