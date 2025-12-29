

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