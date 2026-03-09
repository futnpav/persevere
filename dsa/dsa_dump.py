

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


# # implementing a binary tree that maintains completeness and balance automatically
# # implementation:
# # completeness: 
# # 1) detecting insertion to singleton parent, promoting the new inserted node to the same level with the parent
# # 2) detecting removal of leaf node whose sibling has only one child, promoting the child to the same level as the removed leaf
# # balance: 
# # 1) detecting depth difference between the left and right branches, rebalancing via rolling into the deeper branch when the delta is 
# #    greater than 1. This approach maintains the depth diference between left and right branches to be at most 1, and within root.left
# #    and root.right to be at most 2.
# # Note: value in node may be swapped among nodes to make_complete and make_balance, so nodes shall never be exposed publicly
# # Evolution: oringinally put the depth in each node, simply and intuitive. However, it is really costly for make_balance O(n), defeating
# # the purpose of BST. So left_depth_list and right_depth_list are introduced to keep track of the number of nodes at each depth, reducing
# # Time Complexity to O(log n) for make_balance.
# class BSTCompleteBalanced:
#     def __init__(self):
#         self.root = None
#         self._size = 0
#         self.left_depth_list = []
#         self.right_depth_list = []

#     def is_empty(self):
#         return self._size == 0
    
#     def size(self):
#         return self._size
#     # insert v as for put for b search tree while keeping completeness and balance
#     def put(self, v):
#         def _recursion_helper(n, p, g):
#             nonlocal parentDepth, insert, parent, grand
#             if n is None:
#                 insert = BTNode(v)
#                 parent = p
#                 grand = g
#                 return insert
#             parentDepth = n.depth
#             if n.value > v:
#                 n.left = _recursion_helper(n.left, n, p)
#             else:
#                 n.right = _recursion_helper(n.right, n, p)
#             return n    
#         parentDepth = 0
#         insert = self.root
#         parent = grand = None
#         _recursion_helper(self.root, parent, grand)
#         if(self.root is None):
#             self.root = insert
#         # make complete if parent and grand are both singletons
#         if (grand.left and grand.right) == False and (parent.left and parent.right) == False:
#             self._make_complete(insert, parent, grand)
#         self._increase_depth_list(v, insert.depth)
#         if(abs(self.right_depth_list.count() - self.left_depth_list.count()) > 1):
#             self._make_balance()
#         self._size += 1
#     # can only do with a leaf node
#     def _increase_depth_list(self, v, depth):
#         the_depth_list = self.left_depth_list if self.root.value > v else self.right_depth_list
#         if(depth - 1 > the_depth_list.count()):
#             the_depth_list.append(1)
#         else:
#             the_depth_list[depth - 2] += 1
#     # can only do with a leaf node
#     def _decrease_depth_list(self, v, depth):
#         the_depth_list = self.left_depth_list if self.root.value > v else self.right_depth_list
#         the_depth_list[depth - 2] -= 1
#         if(the_depth_list[depth - 2] == 0):
#             the_depth_list.pop()
#     # move the son to the same level as parent and rearrange the value
#     def _make_complete(self, son, parent, grand):
#         l = [son.value, parent.value, grand.value]
#         l.sort()
#         grand.left = son
#         son.value = l[0]
#         grand.right = parent
#         parent.value = l[2]
#         grand.value = l[1]
#         son.depth -= 1
#     # keep upgrading the first node in the longer_side branch to the root till 
#     # the depth differnece is 1 or less
#     def _make_balance(self):
#         while(abs(self.left_depth_list.count() - self.right_depth_list.count()) > 1):
#             if(self.left_depth_list.count() > self.right_depth_list.count()):
#                 new_root = self.root.left
#                 switch_over = new_root.right
#                 new_root.right = self.root
#                 self.root.left = switch_over
#             longer_side = "left" if self.left_depth_list.count() > self.right_depth_list.count() else "right"
#             shorter_side = "right" if longer_side == "left" else "left"
#             exec("new_root = self.root.{longer_side}")
#             exec("to_hand_over = new_root.{shorter_side}")
#             exec("new_root.{shorter_side} = self.root")
#             exec("self.root.{longer_side} = to_hand_over")
#             exec("self.root = new_root")
#             self.root.depth -= 1
#             exec("increase_depth(self.root.{shorter_side})")
#             exec("decrease_depth(self.root.{longer_side})")
#             exec("self.{longer_side}_depth -= 1")
#             exec("self.{shorter_side}_depth += 1")
        
#     def increase_depth(self, n):
#         if(n is None):
#             return
#         n.depth += 1
#         self.increase_depth(n.left)
#         self.increase_depth(n.right)

#     def decrease_depth(self, n):
#         if(n is None):
#             return
#         n.depth -= 1
#         self.decrease_depth(n.left)
#         self.decrease_depth(n.right)
#     # err if not return True
#     def update_child_depth(p):
#         def _recursion_helper(p):
#             if p is None:
#                 return True
#             if p.left is not None:
#                 p.left.depth = p.depth + 1
#                 return _recursion_helper(p.left)
#             if p.right is not None:
#                 p.right.depth = p.depth + 1
#                 return _recursion_helper(p.right)
#             return False
#         if p is None:
#             return False
#         return _recursion_helper(p)
#     # update the left_depth_list and right_depth_list of the tree 
#     # Doesn't seem to be useful though as depth is updated upon every update
#     def update_branch_depth(self):
#         def _recursion_helper(n, parent_depth):
#             nonlocal cur_deepest
#             if(n is None):
#                 cur_deepest = parent_depth - 1 if parent_depth - 1 > cur_deepest else cur_deepest
#                 return
#             n.depth = parent_depth + 1
#             _recursion_helper(n.left, n.depth)
#             _recursion_helper(n.right, n.depth)
#         if(self.root is None):
#             self.left_depth_list = self.right_depth_list = 0
#         cur_deepest = 0
#         _recursion_helper(self.left, 1)
#         self.left_depth_list = cur_deepest
#         cur_deepest = 0
#         _recursion_helper(self.right, 1)
#         self.right_depth_list = cur_deepest
    
#     def get_smallest(self, n):
#         def _recursion_helper(n):
#             if(n.left is None):
#                 return n
#             return _recursion_helper(n.left)
#         if(n is None):
#             return None
#         return _recursion_helper(n)
    
#     def get_largest(self, n):
#         def _recrusion_helper(n):
#             if(n.right is None):
#                 return n
#             return _recrusion_helper(n.right)
#         if(n is None):
#             return None
#         return _recrusion_helper(n)
#     # return False if p is None or n is not a child of p, otherwise replace ref to n with that to nn in p
#     def _replace_child(self, p, n, nn):
#         if p is None:
#             self.root = nn
#         if p.left == n:
#             p.left == nn
#         if p.right == n:
#             p.right == nn
        
#     # remove only one node with value v while keep completeness and balance.
#     # remove True if one node with value V is successfully found and removed, otherwise False
#     def remove(self, v):
#         def _recursion_helper(p, n):
#             nonlocal the_parent, the_node
#             if(n is None):
#                 return False
#             if(n.value == v):
#                 the_parent = p
#                 the_node = n
#                 return True
#             if(n.value > v):
#                 return _recursion_helper(n, n.left)
#             else:
#                 return _recursion_helper(n, n.right)
        
#         def _get_largest_tracking_parent(p, n):
#             nonlocal parent_largest_left
#             if(n.right is None):
#                 parent_largest_left = p
#                 return n
#             return _get_largest_tracking_parent(n, n.right)
            
#         if(self.is_empty()):
#             return False
#         the_parent = the_node = None
#         if(_recursion_helper(None, self.root) == False):
#             return False
#         # the value to remove is found. 3 scenarios depending on the number of children the node has as follows
#         # 1. no child
#         # Important: if the sibling has only child, _make_complete is needed. This is one of the 
#         # two cases where removal may cause incompleteness 
#         if the_node.left is None and the_node.right is None:
#             self._replace_child(the_parent, the_node, None)
#         # 2. one Child
#         if(the_node.left is None):
#             self.decrease_depth(the_node.right)
#             self._replace_child(the_parent, the_node, the_node.right)
#         if(the_node.right is None):
#             self.decrease_depth(the_node.left)
#             self._replace_child(the_parent, the_node, the_node.left)
#         # 3. both children, replace the node with the largest on its left branch
#         parent_largest_left = None
#         largest_left = _get_largest_tracking_parent(the_node, the_node.left)
#         the_node.value = largest_left.value
#         # the largest_left may have a left child
#         if(largest_left.left is not None):
#             largest_left.value = largest_left.left.value
#             largest_left.left = None
#         else:
#             if(largest_left == parent_largest_left.left):
#                 parent_largest_left.left = None
#             else:
#                 parent_largest_left.right = None

#         self.update_branch_depth()
#         self._make_balance()
#         self._size -= 1

#         # test commit to the new repo iMac 24 then from iMac 27
        
#         return True


from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Iterable, Generator, Any


class Color(Enum):
    RED = 0
    BLACK = 1


@dataclass
class Node:
    key: Any
    color: Color
    left: "Node"
    right: "Node"
    parent: "Node"


class RedBlackTree:
    """
    Red-Black Tree (CLRS-style) with a single shared NIL sentinel.

    Supports:
      - insert(key)
      - delete(key)  (raises KeyError if not found)
      - search(key) -> bool
      - find_node(key) -> Node | None
      - inorder() -> generator of keys
      - min(), max()
    """

    def __init__(self):
        # Create a single NIL sentinel node; its pointers point to itself.
        self.NIL = Node(key=None, color=Color.BLACK, left=None, right=None, parent=None)  # type: ignore
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL
        self.root: Node = self.NIL
        self._size = 0

    def __len__(self) -> int:
        return self._size

    # ---------- Public API ----------

    def search(self, key: Any) -> bool:
        return self.find_node(key) is not None

    def find_node(self, key: Any) -> Optional[Node]:
        cur = self.root
        while cur is not self.NIL:
            if key == cur.key:
                return cur
            cur = cur.left if key < cur.key else cur.right
        return None

    def insert(self, key: Any) -> None:
        # Standard BST insert
        z = Node(key=key, color=Color.RED, left=self.NIL, right=self.NIL, parent=self.NIL)
        y = self.NIL
        x = self.root

        while x is not self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            elif z.key > x.key:
                x = x.right
            else:
                # If you prefer to allow duplicates, you can change this logic.
                return

        z.parent = y
        if y is self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self._size += 1
        self._insert_fixup(z)

    def delete(self, key: Any) -> None:
        z = self.find_node(key)
        if z is None:
            raise KeyError(f"Key not found: {key}")

        y = z
        y_original_color = y.color
        if z.left is self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum_node(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        self._size -= 1
        if y_original_color == Color.BLACK:
            self._delete_fixup(x)

    def inorder(self) -> Generator[Any, None, None]:
        yield from self._inorder_nodes(self.root)

    def min(self) -> Any:
        if self.root is self.NIL:
            raise ValueError("empty tree")
        return self._minimum_node(self.root).key

    def max(self) -> Any:
        if self.root is self.NIL:
            raise ValueError("empty tree")
        return self._maximum_node(self.root).key

    # ---------- Internal helpers ----------

    def _inorder_nodes(self, n: Node) -> Generator[Any, None, None]:
        if n is self.NIL:
            return
        yield from self._inorder_nodes(n.left)
        yield n.key
        yield from self._inorder_nodes(n.right)

    def _minimum_node(self, n: Node) -> Node:
        while n.left is not self.NIL:
            n = n.left
        return n

    def _maximum_node(self, n: Node) -> Node:
        while n.right is not self.NIL:
            n = n.right
        return n

    def _left_rotate(self, x: Node) -> None:
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, x: Node) -> None:
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def _insert_fixup(self, z: Node) -> None:
        # Fix red-red violations upward.
        while z.parent.color == Color.RED:
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right  # uncle
                if y.color == Color.RED:
                    # Case 1: parent and uncle are red -> recolor
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        # Case 2: convert to case 3
                        z = z.parent
                        self._left_rotate(z)
                    # Case 3: rotate + recolor
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._right_rotate(z.parent.parent)
            else:
                # Mirror cases
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._left_rotate(z.parent.parent)

        self.root.color = Color.BLACK

    def _transplant(self, u: Node, v: Node) -> None:
        if u.parent is self.NIL:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_fixup(self, x: Node) -> None:
        # Fix "double black" at x.
        while x is not self.root and x.color == Color.BLACK:
            if x is x.parent.left:
                w = x.parent.right  # sibling
                if w.color == Color.RED:
                    # Case 1
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    # Case 2
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        # Case 3
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self._right_rotate(w)
                        w = x.parent.right
                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                # Mirror cases
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK


if __name__ == "__main__":
    # Quick sanity test
    rbt = RedBlackTree()
    vals = [20, 15, 25, 10, 5, 1, 30, 22, 27, 19]
    for v in vals:
        rbt.insert(v)

    print("Inorder:", list(rbt.inorder()))
    print("Min:", rbt.min(), "Max:", rbt.max(), "Size:", len(rbt))

    for v in [10, 22, 20, 1]:
        rbt.delete(v)
        print(f"After delete {v}:", list(rbt.inorder()), "Size:", len(rbt))

    print("Search 22:", rbt.search(22))
    print("Search 25:", rbt.search(25))




class RBNodeC:
    def __init__(self, v=None, color="red"):
        self.value = v
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RBTreeC:
    def __init__(self):
        self.nil = RBNodeC()
        self.nil.color = "black"
        self.nil.left = self.nil.right = self.nil.parent = self.nil
        self.root = self.nil
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def left_rotate(self, n):
        new_top = n.right
        n.right = new_top.left
        new_top.left = n
        return new_top
    
    def right_rotate(self, n):
        new_top = n.left
        n.left = new_top.right
        new_top.right = n
        return new_top
        