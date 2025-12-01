# List and Arrays
my_list = [3, 45, 6, 1, 6, 8, -9]
minVal = my_list[0]

for i in my_list:
    if i < minVal:
        minVal = i

# print("Minimum value in the list is:", minVal)

# stack
# implement a stack using list
class ArrayStack:
    def __init__(self):
       self._store = []

    def is_empty(self):
        return len(self._store) == 0
        
    def size(self):
        return len(self._store)
        
    def push(self, v):
        self._store.append(v)

    def peek(self):
        if(self.is_empty()):
            return None
        return self._store[self._size() - 1]

    def pop(self):
        if(self.is_empty()):
            return None
        return self._store.pop()
    
s = ArrayStack()
# print("pop a new stack:", s.pop())

s.push(5)
s.push(10)
s.push(15)
s.push(20)

# print("stack size:", s._size())
# print("stack peek:", s.peek())
# print("stack pop:", s.pop())
# print("stack size after pop:", s._size())

# implement a stack using a linked list
class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None

class LinkedListStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def stackSize(self):
        return self._size
    
    def peek(self):
        if(self.is_empty()):
            return None
        return self._top.value
    
    def pop(self):
        if(self.is_empty()):
            return None
        popped_value = self._top_value
        self._top = self._top.next
        self._size -= 1
        return popped_value
    
    def push(self, v):
        new_top = Node(v)
        new_top.next= self._top
        self._top = new_top
        self._size += 1

ls = LinkedListStack()
# print("pop a new linked list stack:", ls.pop())
# print("peek a new linked list stack:", ls.peek())
# print("is it empty?:", ls.is_empty())
# print("size of linked list stack:", ls.stackSize())
# ls.push(100)
# ls.push(200)
# ls.push(300)
# print("peek after pushing 3 elements:", ls.peek())
# print("size after pushing 3 elements:", ls.stackSize())
# print("pop after pushing 3 elements:", ls.pop())
# print("size after popping 1 element:", ls.stackSize())

class ArrayQueue:
    def __init__(self):
        self._store = []

    def is_empty(self):
        return len(self._store) == 0
    
    def size(self):
        return len(self._store)
    
    def enqueue(self, v):
        self._store.append(v)

    def dequene(self):
        if(self.is_empty()):
            return None
        return self._store.pop(0)
    
    def peek(self):
        if(self.is_empty()):
            return None
        return self._store[0]
    

aq = ArrayQueue()
# print("dequeue a new queue:", aq.dequene())
# print("peek a new queue:", aq.peek())
# print("is it empty?:", aq.is_empty())
# print("size of queue:", aq.size())
# aq.enqueue(10)
# aq.enqueue(20)
# aq.enqueue(30)
# print("peek after enqueuing 3 elements:", aq.peek())
# print("size after enqueuing 3 elements:", aq.size())
# print("dequeue after enqueuing 3 elements:", aq.dequene())
# print("size after dequeuing 1 element:", aq.size())

# implement a queue using linked list
class LinkedListQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size
    
    def enqueue(self, v):
        new_node = Node(v)
        if(self.is_empty()):
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def peek(self):
        if(self.is_empty()):
            return None
        return self._head.value
    
    def dequeue(self):
        if(self.is_empty()):
            return None
        popped_value = self._head.value
        if(self.size() == 1):
            self._head = self._tail = None
        else:
            self._head = self._head.next
        self._size -= 1
        return popped_value

lq = LinkedListQueue()
print("dequeue a new linked list queue:", lq.dequeue())
print("peek a new linked list queue:", lq.peek())
print("is it empty?:", lq.is_empty())
print("size of linked list queue:", lq.size())
lq.enqueue(50)
lq.enqueue(100)
lq.enqueue(150)
print("peek after enqueuing 3 elements:", lq.peek())
print("size after enqueuing 3 elements:", lq.size())
print("dequeue after enqueuing 3 elements:", lq.dequeue())
print("size after dequeuing 1 element:", lq.size())

class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._self
    
    def insert(self, i, v):
        if(i < 0 or i > self.size()):
            raise Exception("Index out of bounds")
        new_node = Node(v)
        if(i == 0):
            new_node.next = self._head
            self._head = new_node
        else:
            previous = self._head
            j = 0
            while(j < i - 1):
                previous = previous.next
                j += 1
            new_node.next = previous.next
            previous.next = new_node
        self._size += 1

            








