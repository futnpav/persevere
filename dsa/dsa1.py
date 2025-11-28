# List and Arrays
my_list = [3, 45, 6, 1, 6, 8, -9]
minVal = my_list[0]

for i in my_list:
    if i < minVal:
        minVal = i

print("Minimum value in the list is:", minVal)

# Implementing a stack using a list
class ListStack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if(self.is_empty()):
           return None
        self.stack.pop()

    def peek(self):
        if(self.is_empty()):
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
stack = ListStack()

stack.push(5)
stack.push(10)
stack.push(15)

print("Top element is:", stack.peek())
print("Stack size is:", stack.size())
print("Popped element is:", stack.pop())
print("Stack size after pop is:", stack.size())

class Node:
    def __init__(self,v = None):
        self.value = v
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def size(self):
             return self.size

    def push(self, v):
        if(self.is_empty()):
            self.top = Node(v)
        else:
            new_top = Node(v)
            new_top.next = self.top
            self.top = new_top
        self.size += 1

    def peek(self):
        if(self.is_empty()):
            return None
        return self.top.value
    
    def pop(self):
        if(self.is_empty()):
            return None
        popped = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped
    
    def fetch_all(self):
        current = self.top
        ls = []
        while current is not None:
            ls.append(current.value)
            current = current.next
        return ls
    
ll_stack = LinkedListStack()

ll_stack.push(20)
ll_stack.push(30)
ll_stack.push(40)
print("All elements in linked list stack are:", ll_stack.fetch_all())
print("Top element in linked list stack is:", ll_stack.peek())
print("Linked list stack size is:", ll_stack.size)
print("Popped element from linked list stack is:", ll_stack.pop())
print("Linked list stack size after pop is:", ll_stack.size)

print("All elements in linked list stack are:", ll_stack.fetch_all())

        


