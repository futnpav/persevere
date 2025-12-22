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
        def __init__(self):
            self._store = []
            for _ in range(10):
                self._store.append([])
            self._size = 0

        def _get_index(self, v):
            return hash(v) % 10

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
            if(self._store[index] is None):
                return False
            return v in self._store[index]
        # return v if removed; None if not found
        def remove(self, v):
            if(self.is_empty()):
                return None
            index = self._get_index(v)
            if(self._store[self._get_index(v)] is None):
                return None
            if(v in self._store[self._get_index(v)]):
                self._store[self._get_index(v)].remove(v)
                self._size -= 1
                return v
            return None

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

    # def put(self, v):
    #     if(self.root is None):
    #         self.root = BTNode(v)
    #         self._size += 1
    #         return
    #     current = self.root
    #     while True:
    #         if(current.value > v):
    #             if(current.left is None):
    #                 current.left = BTNode(v)
    #                 self._size += 1
    #                 break
    #             else:
    #                 current = current.left
    #         else:
    #             if(current.right is None):
    #                 current.right = BTNode(v)
    #                 self._size += 1
    #                 break
    #             else:
    #                 current = current.right

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
    
    # return True if found and removed, otherwise False
    # def remove_substitute_closest_small(self, v):
    #     if(self.is_empty()):
    #         return False
    #     parent = None
    #     current = self.root
    #     while(current is not None and current.value != v):
    #         parent = current
    #         if(current.value > v):
    #             current = current.left
    #         else:
    #             current = current.right
    #     if(current is None):
    #         return False
    #     # at this point, current is the node to be removed
    #     # case 1: current has no or only one child
    #     break_at = "left" if parent.left == current else "right"
    #     if(current.left is None and current.right is None):
    #         exec(f"parent.{break_at} = None")
    #     elif(current.left is None):
    #         exec(f"parent.{break_at} = current.right")
    #     elif(current.right is None):
    #         exec(f"parent.{break_at} = parent.left")
    #     # unfortunately two children
    #     else:
    #         # replace current with the closest smaller one
    #         successor_parent = current
    #         successor = current.left
    #         while(successor.right is not None):
    #             successor_parent = successor
    #             successor = successor.right
    #         current.value = successor.value
    #         if(successor_parent == current):
    #             successor_parent.left = successor.left
    #         else:
    #             successor_parent.right = successor.left
    #     self._size -= 1
    #     return True

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


class BTNodeWithDepth:
    def __init__(self, v, d):
        self.value = v
        self.depth = d
        self.left = None
        self.right = None
# each node keeps its own depth starting from 1
# ensure completeness rearranging values in case of insertion to a single parent
# left_depth & right_depth not counting root depth hence starting, e.g. left_depth is 0 when root.left is None
class BSTCompleteBalanced:
    def __init__(self):
        self.root = None
        self._size = 0
        self.left_depth = 0
        self.right_depth = 0

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    # insert v as for put for b search tree while keeping completeness and balance
    def put(self, v):
        def _recursion_helper(n, p, g):
            nonlocal parentDepth, insert, parent, grant
            if n is None:
                insert = BTNodeWithDepth(v, parentDepth + 1)
                parent = p
                grant = g
                return insert
            parentDepth = n.depth
            if n.value > v:
                n.left = _recursion_helper(n.left, n, p)
            else:
                n.right = _recursion_helper(n.right, n, p)
            return n    
        parentDepth = 0 if self.root is None else self.root.depth
        insert = self.root
        parent = grant = None
        _recursion_helper(insert, parent, grant)
        self._size += 1
        if (grant.left and grant.right) is None and (parent.left and parent.right) is None:
            insert_depth = self._make_complete(insert, parent, grant)
        if(self.root.value > v):
            self.left_depth = insert_depth if insert_depth > self.left_depth else self.left_depth
        else:
            self.right_depth = insert_depth if insert_depth > self.right_depth else self.right_depth
        if(abs(self.right_depth - self.left_depth) > 1):
            self._make_balance()
    # move the son to the same level as parent and rearrange the value
    def _make_complete(self, son, parent, grant):
        l = [son.value, parent.value, grant.value]
        l.sort()
        grant.left = son
        son.value = l[0]
        grant.right = parent
        parent.value = l[2]
        grant.value = l[1]
        son.depth -= 1
        return son.depth
    # keep upgrading the first node in the longer_side branch to the root till the depth differnece is 1 or less
    def _make_balance(self):
        while(abs(self.left_depth - self.right_depth) > 1):
            longer_side = "left" if self.left_depth > self.right_depth else "right"
            shorter_side = "right" if longer_side == "left" else "left"
            exec("new_root = self.root.{longer_side}")
            exec("to_hand_over = new_root.{shorter_side}")
            exec("new_root.{shorter_side} = self.root")
            exec("self.root.{longer_side} = to_hand_over")
            exec("self.root = new_root")
            self.root.depth -= 1
            exec("increase_depth_by_one(self.root.{shorter_side})")
            exec("decrease_depth_by_one(self.root.{longer_side})")
            exec("self.{longer_side}_depth -= 1")
            exec("self.{shorter_side}_depth += 1")
        
    def increase_depth_by_one(self, n):
        if(n is None):
            return
        n.depth += 1
        self.increase_depth_by_one(n.left)
        self.increase_depth_by_one(n.right)

    def decrease_depth_by_one(self, n):
        if(n is None):
            return
        n.depth -= 1
        self.decrease_depth_by_one(n.left)
        self.decrease_depth_by_one(n.right)
    # update the depth for all nodes in the tree, based on the root with depth = 1. Doesn't seem to be useful though as depth is updated upon every update
    def update_branch_depth(self):
        def _recursion_helper(n, parent_depth):
            nonlocal cur_deepest
            if(n is None):
                cur_deepest = parent_depth - 1 if parent_depth - 1 > cur_deepest else cur_deepest
                return
            n.depth = parent_depth + 1
            _recursion_helper(n.left, n.depth)
            _recursion_helper(n.right, n.depth)
        if(self.root is None):
            self.left_depth = self.right_depth = 0
        cur_deepest = 0
        _recursion_helper(self.left, 1)
        self.left_depth = cur_deepest
        cur_deepest = 0
        _recursion_helper(self.right, 1)
        self.right_depth = cur_deepest
    
    def get_smallest(self, n):
        def _recursion_helper(n):
            if(n.left is None):
                return n
            return _recursion_helper(n.left)
        if(n is None):
            return None
        return _recursion_helper(n)
    
    def get_largest(self, n):
        def _recrusion_helper(n):
            if(n.right is None):
                return n
            return _recrusion_helper(n.right)
        if(n is None):
            return None
        return _recrusion_helper(n)
        
    # remove only one node with value v while keep completeness and balance.
    # remove True if one node with value V is successfully removed, otherwise False
    def remove(self, v):
        def _recursion_helper(p, n):
            nonlocal the_parent, the_node
            if(n is None):
                return False
            if(n.value == v):
                the_parent = p
                the_node = n
                return True
            if(n.value > v):
                return _recursion_helper(n, n.left)
            else:
                return _recursion_helper(n, n.right) 
        if(self.is_empty()):
            return False 
        the_parent = the_node = None
        if(_recursion_helper(None, self.root) == False):
            return False
        if(the_node.left is None):
            if(the_node.right is None):
                if(the_parent.left == the_node):
                    the_parent.left = None
                else:
                    the_parent.right = None
            else:
                if(the_parent.left == the_node):
                    the_parent.left = the_node.right
                else:
                    the_parent.right = the_node.right
        
        return True

            


