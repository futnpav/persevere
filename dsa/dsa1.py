# List and Arrays
my_list = [3, 45, 6, 1, 6, 8, -9]
minVal = my_list[0]

for i in my_list:
    if i < minVal:
        minVal = i

# print("Minimum value in the list is:", minVal)

# stack
# implement a stack using list
class ListStack:
    def __init__(self):
       self.store = []

    def is_empty(self):
        return len(self.store) == 0
        
    def size(self):
        return len(self.store)
        
    def push(self, v):
        self.store.append(v)

    def peek(self):
        if(self.is_empty()):
            return None
        return self.store[self.size() - 1]

    def pop(self):
        if(self.is_empty()):
            return None
        return self.store.pop()
    
s = ListStack()
print("pop a new stack:", s.pop())

s.push(5)
s.push(10)
s.push(15)
s.push(20)

# print("stack size:", s.size())
# print("stack peek:", s.peek())
# print("stack pop:", s.pop())
# print("stack size after pop:", s.size())

# implement a stack using a linked list

