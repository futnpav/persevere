"""
This case study reveals interesting findings on how ChatGPT copes with novice solutions to a known
problem. 
Code under test:
A alternative solution to the classic RB Tree problem with the following modifications:
    1. removal of the pointer/reference to the parent node
    2. replacement of while loop for searching with recursive algorithm, which eliminates the need
    reference to the parent node
    3. replacement of the self-referencing sentinel nil node with None terminated ones
LLM under test: ChatGPT 5.0
Findings:
    I posted my solution to ChatGPT for assessment, and it was very unhappy about the use of the 
    None terminated nil nodes. When I asked it to provide an example where nil terminated nodes 
    may fail it gave the following:
    quote from conversation(start...):
        Step-by-step example: deletion fix-up where sibling is the sentinel
        Consider this very common situation during deletion:

                    n(B)
                    /   \
                child  nil
                (DB)   (B)

        Meaning:
        n is black
        child is the subtree where a black node was removed and now you have a double-black (conceptually)
        the sibling is missing, so it's nil
        This happens when deleting from a parent that effectively had only one real child.
    quote end (...end)

    When I pointed out that:
    start...:
        1. in deletion, there is NO case that a double black node has a nil sibling, if you start with a 
        correct rb tree. Therefore, the worries for accessing children of nil node doesn't exist
    ...end

    ChatGPT admits:
    start...:
        You're right to challenge that example. For a correct red-black tree (with standard definition 
        where all missing children are the same black nil leaf), your comment (1) is essentially correct: 
        during deletion fix-up, the double-black node cannot have a nil sibling. My earlier “DB with nil 
        sibling” picture is not a reachable state from a valid RB tree using the standard delete procedure.
    ...end
Verdict:
    ChatGPT is very strong in reasoning and able to correct errors in its answers. However its reasoning
    lacked the depth as its job required and turned to miss out important factors when it gives answers. In
    this case, it missed out that the example it was asked to provide was to be evaluated 
    in the solution to the RB Tree problem.
Note: I am new to python and still adapting to the pythonic coding style :p
"""
# implement a queue using linked list
class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None
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
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = self._tail.next
        self._size += 1

    def peek(self):
        if self.is_empty():
            return None
        return self._head.value
    
    def dequeue(self):
        if self.is_empty():
            return None
        popped_value = self._head.value
        if self.size() == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
        self._size -= 1
        return popped_value
    
class RBNode:
    def __init__(self, v = None, color : str = "red"):
        self.value = v
        self.color = color  # "red", "black", or "double black"
        self.left = None
        self.right = None
class RBTree:
    def __init__(self):
        self.nil = RBNode(color = "black")
        self.root = self.nil
        self._size = 0

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
            nonlocal grandchild, child, resolved, need_attention
            if n is self.nil:
                new_node = RBNode(v)
                new_node.left = new_node.right = self.nil
                grandchild = new_node
                self._size += 1
                return new_node
            elif v < n.value:
                n.left = _recursion_helper(n.left)
            else:
                n.right = _recursion_helper(n.right)
            # now check for violations and fix
            if resolved:
                return n
            if child is self.nil:
                child = n
                need_attention = True
                return n
            else:
                # handle violations
                if grandchild.color == "red":
                    if child.color == "red":
                        other_child = n.right if child == n.left else n.left
                        if other_child is self.nil or other_child.color == "black":
                            # rotation cases
                            if child == n.left:
                                if grandchild == child.left:
                                    new_top = self.right_rotate(n)
                                else:
                                    n.left = self.left_rotate(child)
                                    new_top = self.right_rotate(n)
                            else:
                                if grandchild == child.right:
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
                            other_child.color = "black"
                            n.color = "red"
                            grandchild = child
                            child = n
                            return n
                    else:
                        if need_attention: # insertion doesn't cause red red conflick, terminate checking
                            resolved = True
                            need_attention = False # not needded practically, only needed for logic mysophobia
            grandchild = child
            child = n
            return n
        if(self.root is self.nil):
            self.root = RBNode(v, "black")
            self.root.left = self.root.right = self.nil
            self._size += 1
        else:
            grandchild = child = self.nil
            resolved = need_attention = False
            self.root = _recursion_helper(self.root)
        self.root.color = "black"
    # remove node in case of nil or one child returns deleted:bool
    def remove(self, v):
        # remove node in case of nil or one child
        # replace value with that of in order successor in case of two children
        # return deleted:bool, db_color:bool, and the new/updated node in the place of the removed
        # db_color indicate whether the new/updated node is double black
        def _recursion_helper(p, n):
            if n is self.nil:
                return False, False, self.nil
            elif v < n.value:
                deleted, db_returned, n.left = _recursion_helper(n, n.left)
                last_node = n.left
            elif v > n.value:
                deleted, db_returned, n.right = _recursion_helper(n, n.right)
                last_node = n.right
            else:
                deleted_node = n
                db_returned = False
                if n.left is not self.nil and n.right is not self.nil:
                    db_returned, n = self._replace_value_with_inorder_successor(n)
                    return True, db_returned, n
                else:
                    if n.left is self.nil:
                        replacement_node = n.right
                    else:
                        replacement_node = n.left
                    if deleted_node.color == "black":
                        if(replacement_node.color == "red"):
                            replacement_node.color = "black"
                        else:
                            db_returned = True
                    return True, db_returned, replacement_node
            if db_returned:
                db_returned, replacement_node = self._fix_double_black_child(n, last_node)
                return deleted, db_returned, replacement_node
            return deleted, db_returned, n
        if self.is_empty():
            return False
        deleted, db_top, self.root = _recursion_helper(None, self.root)
        # if(db_returned):
        #     self.root.color = "black"
        if deleted:
            self._size -= 1
        return deleted
    # set the t.value to that of in order successor and remove the successor
    # return the db_color:bool and updated t
    # Assumption: t has both children
    def _replace_value_with_inorder_successor(self, t):
        def _recursion_helper(n):
            if n.left is self.nil:
                t.value = n.value
                db_returned = False
                if n.color == "black":
                    if n.right.color == "red":
                        n.right.color = "black"
                    else:
                        db_returned = True
                return db_returned, n.right
            db_returned, n.left = _recursion_helper(n.left)
            if db_returned:
                return self._fix_double_black_child(n, n.left)
            return False, n
        db_returned, t.right = _recursion_helper(t.right)
        if db_returned:
            return self._fix_double_black_child(t, t.right)
        return False, t
    # fix the double black child
    # returns db_returned:bool, new_top(at the place of n)
    # db_returned == True indicates double black has been bubbled up from child to new_top
    def _fix_double_black_child(self, n, child):
        db_returned = False
        sibling = n.left if n.right == child else n.right
        # red sibling, rotate inwards: sibling becomes new_top, its medial child becomes new sibling
        if sibling.color == "red": # indicates black for n, sibling.left and sibling.right
            if n.left == child:
                new_top = self.left_rotate(n)
                new_top.color = "black"
                n.color = "red"
                db_returned, new_top.left = self._fix_double_black_child(n, child)
            else:
                new_top = self.right_rotate(n)
                new_top.color = "black"
                n.color = "red"
                db_returned, new_top.right = self._fix_double_black_child(n, child)
            return db_returned, new_top # db_returned shall always be False
        else: # black sibling
            if n.left == child: # double black on the left side
                if sibling.right.color == "red": # lateral red sibling child
                    new_top = self.left_rotate(n)
                    new_top.color = n.color
                    new_top.right.color = "black"
                    n.color = "black"
                    child.color = "black"
                elif sibling.left.color == "red": # medial red sibling child
                    n.right = self.right_rotate(sibling)
                    new_top = self.left_rotate(n)
                    new_top.color = n.color
                    n.color = "black"
                    child.color = "black"
                else:
                    new_top = n
                    child.color = "black"
                    sibling.color = "red"
                    if(n.color == "red"):
                        n.color = "black"
                    else:
                        db_returned = True
            else: # double black on the right side
                if sibling.left.color == "red":
                    new_top = self.right_rotate(n)
                    new_top.color = n.color
                    new_top.left.color = "black"
                    n.color = "black"
                    child.color = "black"
                elif sibling.right.color == "red":
                    n.left = self.left_rotate(sibling)
                    new_top = self.right_rotate(n)
                    new_top.color = n.color
                    n.color = "black"
                    child.color = "black"
                else:
                    new_top = n
                    child.color = "black"
                    sibling.color = "red"
                    if(n.color == "red"):
                        n.color = "black"
                    else:
                        db_returned = True
            return db_returned, new_top

    # dump list of nodes as tuple (level, value, color, left_child_value, right_child_value)
    def bfs_dump(self):
        output = []
        if self.is_empty():
            return []
        q = LinkedListQueue()
        q.enqueue((0, self.root))
        while not q.is_empty():
            level, n = q.dequeue()
            t = (level, n.value, n.color, n.left.value, n.right.value)
            output.append(t)
            if(n.left is not self.nil):
                q.enqueue((level+1, n.left))
            if(n.right is not self.nil):
                q.enqueue((level+1, n.right))
        return output
    
    def print_dump(self):
        d = self.bfs_dump()
        while len(d):
            print(d.pop(0))

rb = RBTree()
rb.put(0)
rb.put(1)
rb.put(2)
rb.put(3)
rb.put(4)
rb.put(5)

# d = rb.bfs_dump()
# while len(d):
#     print(d.pop(0))

rb.remove(1)

d = rb.bfs_dump()
while len(d):
    print(d.pop(0))