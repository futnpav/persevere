import math

# List and Arrays
my_list = [3, 45, 6, 1, 6, 8, -9]
minVal = my_list[0]

for i in my_list:
    if i < minVal:
        minVal = i

# print("Minimum value in the list is:", minVal)

# rights
# implement a rights using list
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
# print("pop a new rights:", s.pop())

# s.push(5)
# s.push(10)
# s.push(15)
# s.push(20)

# print("rights size:", s._size())
# print("rights peek:", s.peek())
# print("rights pop:", s.pop())
# print("rights size after pop:", s._size())

# implement a rights using a linked list
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
    
    def rightsSize(self):
        return self._size
    
    def peek(self):
        if(self.is_empty()):
            return None
        return self._top.value
    
    def pop(self):
        if(self.is_empty()):
            return None
        popped_value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return popped_value
    
    def push(self, v):
        new_top = Node(v)
        new_top.next= self._top
        self._top = new_top
        self._size += 1

# ls = LinkedListStack()
# print("pop a new linked list rights:", ls.pop())
# print("peek a new linked list rights:", ls.peek())
# print("is it empty?:", ls.is_empty())
# print("size of linked list rights:", ls.rightsSize())
# ls.push(100)
# ls.push(200)
# ls.push(300)
# print("peek after pushing 3 elements:", ls.peek())
# print("size after pushing 3 elements:", ls.rightsSize())
# print("pop after pushing 3 elements:", ls.pop())
# print("size after popping 1 element:", ls.rightsSize())

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
    

# aq = ArrayQueue()
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
            self._tail = self._tail.next
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

# lq = LinkedListQueue()
# print("dequeue a new linked list queue:", lq.dequeue())
# print("peek a new linked list queue:", lq.peek())
# print("is it empty?:", lq.is_empty())
# print("size of linked list queue:", lq.size())
# lq.enqueue(50)
# lq.enqueue(100)
# lq.enqueue(150)
# print("peek after enqueuing 3 elements:", lq.peek())
# print("size after enqueuing 3 elements:", lq.size())
# print("dequeue after enqueuing 3 elements:", lq.dequeue())
# print("size after dequeuing 1 element:", lq.size())

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
    
# ll = LinkedList()
# print("is linked list empty?:", ll.is_empty())
# print("size of linked list:", ll.size())
# ll.insert(0, 10)
# ll.insert(1, 30)
# ll.insert(1, 2)
# print("linked list after inserting 3 elements:", ll.traverse())
# print("retrieve element at index 1:", ll.retrieve(1))
# print("size after inserting 3 elements:", ll.size())
# print("remove element at index 1:", ll.remove(1))
# print("linked list after removing element at index 1:", ll.traverse())
# ll.append(4)
# ll.append(2)
# ll.append(5)
# print("linked list after appending 3 elements:", ll.traverse())
# ll.sort(True)
# print("linked list after sorting in ascending order:", ll.traverse())
        

class HashTable:
        def __init__(self, store_size = 1000):
            self._store = []
            for _ in range(store_size):
                self._store.append([])
            self._size = 0

        def _get_index(self, v):
            return hash(v) % len(self._store)

        def is_empty(self):
            return self._size == 0
        
        def size(self):
            return self._size
        
        def put(self, v):
            self._store[self._get_index(v)].append(v)
            self._size += 1

        def has(self, v):
            if(self.is_empty()):
                return False
            index = self._get_index(v)
            if(len(self._store[index]) == 0):
                return False
            return v in self._store[index]
        # return True if removed; False if not found
        def remove(self, v):
            if(self.is_empty()):
                return False
            index = self._get_index(v)
            if(len(self._store[index]) == 0):
                return False
            if(v in self._store[index]):
                self._store[index].remove(v)
                self._size -= 1
                return True
            return False

# ht = HashTable()
# print("is hash table empty?:", ht.is_empty())
# print("size of hash table:", ht.size())
# ht.put("apple")
# ht.put("banana")
# ht.put("orange")
# print(ht._store)
# print("size after putting 3 elements:", ht.size())
# print("has 'banana'?:", ht.has("banana"))
# print("remove 'banana':", ht.remove("banana"))
# print("has 'banana' after removal?:", ht.has("banana"))
# print("size after removing 'banana':", ht.size())

class BTNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
# allow duplicate values, which are dropped down
class BST:
    def __init__(self):
        self.root = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size

    def put(self, v):
        def _recursion_helper(n):
            if(n is None):
                return BTNode(v)
            if(n.value > v):
                n.left = _recursion_helper(n.left)
            else:
                n.right = _recursion_helper(n.right)
            return n
        self.root = _recursion_helper(self.root)
        self._size += 1


    def bfs_traversal_queue(self):
        if(self.is_empty()):
            return []
        result = []
        queue = LinkedListQueue()
        queue.enqueue(self.root)
        while(not queue.is_empty()):
            head = queue.dequeue()
            result.append(head.value)
            if(head.left is not None):
                queue.enqueue(head.left)
            if(head.right is not None):
                queue.enqueue(head.right)
        return result
    
    def bfs_traversal_recursive(self):
        if(self.is_empty()):
            return []
        result = []
        queue = LinkedListQueue()
        queue.enqueue(self.root)
        def _recursion_helper():
            if(queue.is_empty()):
                return
            head = queue.dequeue()
            result.append(head.value)
            if(head.left is not None):
                queue.enqueue(head.left)
            if(head.right is not None):
                queue.enqueue(head.right)
            _recursion_helper()
        _recursion_helper()
        return result
    # pre-order traversal starting from bottom left
    def dfs_traversal_stack(self):
        if(self.is_empty()):
            return []
        result = []
        rights = LinkedListStack()
        rights.push(self.root)
        while(not rights.is_empty()):
            current = rights.pop()
            while(current is not None):
                result.append(current.value)
                if(current.right is not None):
                    rights.push(current.right)
                current = current.left
        return result
    # post-order traversal by recursion
    def dfs_traversal_recursive(self):
        if(self.is_empty()):
            return []
        result = []
        def _recursion_helper(n):
            if(n is None):
                return
            _recursion_helper(n.left)
            _recursion_helper(n.right)
            result.append(n.value)
        _recursion_helper(self.root)
        return result
    
    def dfs_has_recursive(self, v):
        if(self.is_empty()):
            return False
        def _recursion_helper(n):
            if(n is None):
                return False
            if(n.value == v):
                return True
            if(n.value > v):
                return _recursion_helper(n.left)
            else:
                return _recursion_helper(n.right)
        return _recursion_helper(self.root)

    def get_smallest(self, n):
        def _recursion_helper(n):
            if(n is None):
                return n
            if(n.left is None):
                return n
            return _recursion_helper(n.left)
        return _recursion_helper(n)
    
    def get_largest(self, n):
        def _recursion_helper(n):
            if(n is None):
                return n
            if(n.right is None):
                return n
            return _recursion_helper(n.right)
        return _recursion_helper(n)
    
    # return True if found and removed, otherwise False
    def remove_left_branch_up(self, v):
        # break when found or hit the bottom
        found = False
        def _recursion_helper(n):
            nonlocal found
            if(n is None):
                return None
            if(n.value == v):
                found = True
                if(n.right is None):
                    return n.left
                else:
                    if(n.left is None):
                        return n.right
                    else:
                        largestInLeftBranch = self.get_largest(n.left)
                        largestInLeftBranch.right = n.right
                        return n.left
            if(n.value > v):
                n.left = _recursion_helper(n.left)
            else:
                n.right = _recursion_helper(n.right)
            return n        
        _recursion_helper(self.root)
        if(found == True):
            self._size -= 1
        return found
        
# bst = BST()
# bst.put(50)
# bst.put(30)
# bst.put(70)
# bst.put(20)
# bst.put(40)
# bst.put(60)
# bst.put(80)
# bst.put(50)
# print("BFS Traversal using Queue:", bst.bfs_traversal_queue())
# print("BFS Traversal using Recursion:", bst.bfs_traversal_recursive())
# print("DFS Traversal using Stack:", bst.dfs_traversal_stack())
# print("DFS Traversal using Recursion:", bst.dfs_traversal_recursive())
# print("DFS Has 60 using Recursion:", bst.dfs_has_recursive(100))
# print("Remove 50 left branch up:", bst.remove_left_branch_up(50))
# print("BFS Traversal after removal:", bst.bfs_traversal_queue())
# print("BFS Traversal using Queue:", bst.bfs_traversal_queue())
# print("BFS Traversal using Recursion:", bst.bfs_traversal_recursive())
# print("DFS Traversal using Stack:", bst.dfs_traversal_stack())
# print("DFS Traversal using Recursion:", bst.dfs_traversal_recursive())
# print("DFS Has 60 using Recursion:", bst.dfs_has_recursive(100))


class AVLNode:
    def __init__(self, v = None):
        self.value = v
        self.height = 1
        self.left = None
        self.right = None
# allows duplicate values, which are dropped to the right. Deletion removes
# the first found occurrence.
class AVLTree:
    def __init__(self):
        self.root = None
        self._size = 0
        
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def get_height(self, n):
        if(n is None):
            return 0
        return n.height
    
    def get_balance_factor(self, n):
        if n is None:
            return 0
        return self.get_height(n.left) - self.get_height(n.right)
    
    def right_rotate(self, top):
        if top is None or top.left is None:
            raise Exception("can't rotate on None top or None top.left")
        new_top = top.left
        hand_over = new_top.right
        new_top.right = top
        top.left = hand_over
        top.height = 1 + max(self.get_height(top.left), self.get_height(top.right))
        new_top.height = 1 + max(self.get_height(new_top.left), self.get_height(new_top.right))
        return new_top
    
    def left_rotate(self, top):
        if top is None or top.right is None:
            raise Exception("can't rotate on None top or None top.right")
        new_top = top.right
        hand_over = new_top.left
        new_top.left = top
        top.right = hand_over
        top.height = 1 + max(self.get_height(top.left), self.get_height(top.right))
        new_top.height = 1 + max(self.get_height(new_top.left), self.get_height(new_top.right))
        return new_top
    
    def put(self, v):
        def recursion_helper(n):
            if(n is None):
                return AVLNode(v)
            if(v < n.value):
                n.left = recursion_helper(n.left)
            else:
                n.right = recursion_helper(n.right)
            n.height = 1 + max(self.get_height(n.left), self.get_height(n.right))
            n = self._rebalance(n)
            return n
        if self.root is None:
            self.root = AVLNode(v)
        else:
            self.root = recursion_helper(self.root)
        self._size += 1
    # check the balance from top downwards, rebalance and adjust heights afterwwards should inbalance be found.
    # return the new top after rebalancing (thru rotation)
    def _rebalance(self, top):
        bf = self.get_balance_factor(top)
        if(bf > 1):
            if(self.get_balance_factor(top.left) >= 0):
                return self.right_rotate(top)
            else:
                top.left = self.left_rotate(top.left)
                return self.right_rotate(top)
        if(bf < -1):
            if(self.get_balance_factor(top.right) <= 0):
                return self.left_rotate(top)
            else:
                 top.right = self.right_rotate(top.right)
                 return self.left_rotate(top)
        return top

    def remove(self, v):
        def recursion_helper(n):
            the_largest = None
            nonlocal deleted
            def pop_largest(n):
                nonlocal the_largest
                if(n is None):
                    return None
                if(n.right is None):
                    the_largest = n
                    return n.left
                n.right = pop_largest(n.right)
                n.height = 1 + max(self.get_height(n.left), self.get_height(n.right))
                return self._rebalance(n)
            if n is None: # not found
                return None
            if v < n.value:
                n.left = recursion_helper(n.left)
            elif v > n.value:
                n.right = recursion_helper(n.right)
            else:  # now n is the node to be removed
                deleted = True
                if(n.left is None):
                    return n.right
                elif(n.right is None):
                    return n.left
                else:
                    n.left = pop_largest(n.left)
                    n.value = the_largest.value
            n.height = 1 + max(self.get_height(n.left), self.get_height(n.right))
            return self._rebalance(n)
        if self.root is None:
            return False
        else:
            deleted = False
            self.root = recursion_helper(self.root)
            self._size -= 1 if deleted else 0
            return deleted
        
    def bfs_traversal_queue(self):
        if(self.is_empty()):
            return []
        result = []
        queue = LinkedListQueue()
        queue.enqueue(self.root)
        while(not queue.is_empty()):
            head = queue.dequeue()
            result.append(head.value)
            if(head.left is not None):
                queue.enqueue(head.left)
            if(head.right is not None):
                queue.enqueue(head.right)
        return result
    # order can be "inorder", "preorder", "postorder"
    def dfs_traversal_recursive(self, order : str = "inorder"):
        if(self.is_empty()):
            return []
        result = []
        def _recursion_helper(n):
            if(n is None):
                return
            if(order == "preorder"):
                result.append(n.value)
            _recursion_helper(n.left)
            if(order == "inorder"):
                result.append(n.value)
            _recursion_helper(n.right)
            if(order == "postorder"):
                result.append(n.value)
        _recursion_helper(self.root)
        return result
    
    # order can be "inorder", "preorder", "postorder"
    def dfs_traversal_recursive_2(self, order : str = "inorder"):
        if(self.is_empty()):
            return []
        result = []
        def _recursion_helper(n):
            return [n.value] if order == "preorder" else [] + \
                    _recursion_helper(n.left) + \
                    [n.value] if order == "inorder" else [] + \
                    _recursion_helper(n.right) + \
                    [n.value] if order == "postorder" else []
        result = _recursion_helper(self.root)
        return result

# avl = AVLTree()
# avl.put(30)
# avl.put(20)
# avl.put(25)
# avl.put(10)
# avl.put(40)
# avl.put(50)
# avl.put(5)
# print("BFS Traversal using Queue:", avl.bfs_traversal_queue())
# avl.remove(30)
# print("BFS Traversal after removing 30:", avl.bfs_traversal_queue())
# avl.remove(10)
# print("BFS Traversal after removing 10:", avl.bfs_traversal_queue())
# avl.remove(25)
# print("BFS Traversal after removing 25:", avl.bfs_traversal_queue())
# avl.remove(100)
# print("BFS Traversal after removing 100 (not found):", avl.bfs_traversal_queue())
# print("Size of AVL Tree:", avl.size())
# print("Is AVL Tree empty?:", avl.is_empty())
# print("DFS Inorder Traversal:", avl.dfs_traversal_recursive("inorder"))
# print("DFS Preorder Traversal:", avl.dfs_traversal_recursive("preorder"))
# print("DFS Postorder Traversal:", avl.dfs_traversal_recursive("postorder"))

class NilRBNode():
    def __init__(self, color : str = "black"):
        self.value = None
        self.color = "black"  # "red", "black", or "double black"
        self.left = None
        self.right = None
class RBNode:
    def __init__(self, v = None, color : str = "red"):
        self.value = v
        self.color = color  # "red", "black", or "double black"
        self.left = NilRBNode()
        self.right = NilRBNode()
# prevents duplicate values, using a hash table to help detect duplicates on insertion
class RBTree:
    def __init__(self):
        self.root = NilRBNode()
        self._size = 0
        self.table = HashTable()

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def left_rotate(self, top):
        new_top = top.right
        hand_over = new_top.left
        top.right = hand_over
        new_top.left = top
        return new_top
    
    def right_rotate(self, top):
        new_top = top.left
        hand_over = new_top.right
        top.left = hand_over
        new_top.right = top
        return new_top
    
    def put(self, v):
        def _recursion_helper(n):
            nonlocal grandchild, child, resolved, just_inserted
            if(isinstance(n, NilRBNode)):
                new_node = RBNode(v)
                grandchild = new_node
                return new_node
            elif(v < n.value):
                n.left = _recursion_helper(n.left)
            else:
                n.right = _recursion_helper(n.right)
            # now check for violations and fix
            if(resolved):
                return n
            if(isinstance(child, NilRBNode)):
                child = n
                just_inserted = True
                return n
            else:
                # handle violations
                if(grandchild.color == "red"):
                    if(child.color == "red"):
                        sibling = n.right if child == n.left else n.left
                        if(isinstance(sibling, NilRBNode) or sibling.color == "black"):
                            # rotation cases
                            if(child == n.left):
                                if(grandchild == child.left):
                                    new_top = self.right_rotate(n)
                                else:
                                    n.left = self.left_rotate(child)
                                    new_top = self.right_rotate(n)
                            else:
                                if(grandchild == child.right):
                                    new_top = self.left_rotate(n)
                                else:
                                    n.right = self.right_rotate(child)
                                    new_top = self.left_rotate(n)
                            new_top.color = "black"
                            new_top.left.color = "red"
                            new_top.right.color = "red"
                            resolved = True # red red conflict resolved locally, terminate checking
                            return new_top
                        else:
                            # swap the color between n and both children, double red is removed but
                            # n is red now. Need to bubble up the checking
                            child.color = "black"
                            sibling.color = "black"
                            n.color = "red"
                            grandchild = child
                            child = n
                            return n
                    else:
                        if just_inserted: # insertion doesn't cause red red conflick, terminate checking
                            resolved = True
                            just_inserted = False # not needded practically, only needed for logic mysophobia
            return n
        if(self.table.has(v)):
            return False
        if(isinstance(self.root, NilRBNode)):
            self.root = RBNode(v, "black")
        else:
            grandchild = child = NilRBNode()
            resolved = just_inserted = False
            self.root = _recursion_helper(self.root)
        self.root.color = "black"
            
    def remove(self, v):
        def _recursion_helper(p, n):
            if(v < n.value):
                n.left = _recursion_helper(n, n.left)
                node_to_check = n.left
            elif(v > n.value):
                n.right = _recursion_helper(n, n.right)
                node_to_check = n.right
            else:
                if(isinstance(n.left, NilRBNode)):
                    if(isinstance(n.right, NilRBNode)):
                        nil = NilRBNode()
                        if n.color == "black":
                            nil.color = "double black"
                        return nil
                    else:
                        if(n.color == "black"):
                            if(n.right.color == "black"):
                                n.right.color = "double black"
                            else:
                                n.right.color = "black"
                        return n.right
                elif(isinstance(n.right, NilRBNode)):
                    if n.color == "black":
                        if(n.left.color == "black"):
                            n.left.color = "double black"
                        else:
                            n.left.color = "black"
                    return n.left
                else:
                    # replace value with inorder successor
                    return self._replace_with_inorder_successor(n)
            if node_to_check.color == "double black":
                return _fix_double_black_child(n, node_to_check)
            return n   
        if self.is_empty() or not self.table.has(v):
            return False
        self.root = _recursion_helper(None, self.root)
        if self.root.color == "double black":
            self.root.color = "black"
        self.table.remove(v)
        self._size -= 1
        return True
    # replace t.value with that of the inorder successor, fix balance or bubble up double black afterwords
    # requires: t.right is not nil
    def _replace_with_inorder_successor(self, t):
        def _recursion_helper(n):
            if(isinstance(n.left, NilRBNode)):
                t.value = n.value
                if(n.color == "black"):
                    if n.right.color == "black":
                        n.right.color = "double black"
                    else:
                        n.right.color = "black"
                return n.right
            n.left = _recursion_helper(n.left)
            if(n.left.color == "double black"):
                n = self._fix_double_black_child(n, n.left)
            return n
        t.right = _recursion_helper(t.right)
        if(t.right.color == "double black"):
            t = self._fix_double_black_child(t, t.right)
        return t
    # fix the double black node n, if can't fix move the double black flag to p
    def _fix_double_black_child(self, n, child):
        sibling = n.left if n.right == child else n.right
        # red sibling, rotate inwards: sibling becomes new_top, its medial child becomes new sibling
        if sibling.color == "red": # indicates black for n, sibling.left and sibling.right
            if n.left == child:
                new_top = self.left_rotate(n)
            else:
                new_top = self.right_rotate(n)
            new_top.color = "black"
            n.color = "red"
            if n.left == child:
                new_top.left = self._fix_double_black_child(n, child)
            else:
                new_top.right = self._fix_double_black_child(n, child)
            return new_top
        else: # black sibling
            if n.left == child: # double black on the left side
                if(not isinstance(sibling.right, NilRBNode) and sibling.right.color == "red"): # lateral red sibling child
                    new_top = self.left_rotate(n)
                    new_top.color = n.color
                    new_top.right.color = "red"
                    n.color = "black"
                    child.color = "black"
                elif(not isinstance(sibling.left, NilRBNode) and sibling.left.color == "red"): # medial red sibling child
                    n.right = self.right_rotate(sibling)
                    new_top = self.left_rotate(n)
                    new_top.color = n.color
                    n.color = "black"
                    child.color = "black"
            else: # double black on the right side
                if(not isinstance(sibling.left, NilRBNode) and sibling.left.color == "red"):
                    new_top = self.right_rotate(n)
                    new_top.color = n.color
                    new_top.left.color = "black"
                    n.color = "black"
                    child.color = "black"
                elif(not isinstance(sibling.right, NilRBNode) and sibling.right.color == "red"):
                    n.left = self.left_rotate(sibling)
                    new_top = self.right_rotate(n)
                    new_top.color = n.color
                    n.color = "black"
                    child.color = "black"
            if((isinstance(sibling.left, NilRBNode) or sibling.left.color == "black") and \
                (isinstance(sibling.right, NilRBNode) or sibling.right.color == "black")):
                new_top = n
                child.color = "red"
                if(n.color == "red"):
                    n.color = "black"
                else:
                    n.color = "double black"
            return new_top


