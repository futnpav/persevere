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

# implement a linked list. NOTE: INDEX STARTING AT 0
class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def _validIndex(self, i : int):
        if(i < 0 or i >= self.size()):
            raise Exception("Index out of bounds")
        
    def _validIndex2Insert(self, i : int):
        if(i < 0 or i > self.size()):
            raise Exception("Invalid index for insertion")
    
    # return the node at index i (internal use only)
    def _seek(self, i : int) -> Node:
        if(self.is_empty()):
            return None
        self._validIndex(i)
        current = self._head
        j = 0
        while(j < i):
            current = current.next
            j += 1
        return current
    
    def append(self, v):
        if(self.is_empty()):
            self._head = Node(v)
        else:
            current = self._head
            while(current.next is not None):
                current = current.next
            current.next = Node(v)
        self._size += 1
   
    def retrieve(self, i : int):
        return self._seek(i).value
    
    def insert(self, i : int, v):
        new_node = Node(v)
        if(i == 0):
            new_node.next = self._head
            self._head = new_node
        else:
            self._validIndex2Insert(i)
            previous = self._seek(i - 1)
            new_node.next = previous.next
            previous.next = new_node
        self._size += 1

    # remove and return the value at index i
    def remove(self, i : int):
        if(self.is_empty()):
            return None
        self._validIndex(i)
        removed_value = None
        if(i == 0):
            removed_value = self._head.value
            self._head = self._head.next
        else:
            previous = self._seek(i - 1)
            removed_value = previous.next.value
            previous.next = previous.next.next
        self._size -= 1
        return removed_value
    
    # sort the value in linked list, NOT THE NODES
    def sort(self, ascending : bool = True):
        if(self.is_empty()):
            return False
        if(self.size() == 1):
            return True
        for i in range(1, self.size()):
            for j in range(1, self.size() - i + 1):
                front_node = self._seek(j - 1)
                this_node = self._seek(j)
                if((front_node.value <= this_node.value) != ascending):
                    temp = front_node.value
                    front_node.value = this_node.value
                    this_node.value = temp
                j += 1
            i += 1
        return True
    
    def traverse(self):
        values = []
        current = self._head
        while(current is not None):
            values.append(current.value)
            current = current.next
        return values
    
ll = LinkedList()
print("is linked list empty?:", ll.is_empty())
print("size of linked list:", ll.size())
ll.insert(0, 10)
ll.insert(1, 30)
ll.insert(1, 2)
print("linked list after inserting 3 elements:", ll.traverse())
print("retrieve element at index 1:", ll.retrieve(1))
print("size after inserting 3 elements:", ll.size())
print("remove element at index 1:", ll.remove(1))
print("linked list after removing element at index 1:", ll.traverse())
ll.append(4)
ll.append(2)
ll.append(5)
print("linked list after appending 3 elements:", ll.traverse())
ll.sort(True)
print("linked list after sorting in ascending order:", ll.traverse())
        


            








