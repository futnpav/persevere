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
