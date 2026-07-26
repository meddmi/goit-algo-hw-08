from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AVLNode:
    """A single node in an AVL tree."""

    value: int
    left: AVLNode | None = None
    right: AVLNode | None = None
    height: int = 1


class AVLTree:
    """AVL tree implementation for integer values."""

    def __init__(self) -> None:
        """Create an empty AVL tree."""
        self.root: AVLNode | None = None

    def insert(self, value: int) -> None:
        """Insert a value into the AVL tree."""
        self.root = self._insert(self.root, value)

    def delete(self, value: int) -> None:
        """Delete a value from the AVL tree if it exists."""
        self.root = self._delete(self.root, value)

    def _delete(self, node: AVLNode | None, value: int) -> AVLNode | None:
        """Delete a value and rebalance the subtree."""
        if not node:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        self._update_height(node)

        balance = self._balance(node)

        if balance > 1:
            if self._balance(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if self._balance(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _find_min(self, node: AVLNode) -> AVLNode:
        """Find the node with the smallest value in a subtree."""
        current = node

        while current.left is not None:
            current = current.left

        return current

    def _insert(self, node: AVLNode | None, value: int) -> AVLNode:
        """Insert a value and rebalance the subtree."""
        if not node:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node

        self._update_height(node)

        balance = self._balance(node)

        if balance > 1:
            if value < node.left.value:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if value > node.right.value:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, value: int) -> bool:
        """Return True if the value exists in the AVL tree."""
        current = self.root

        while current is not None:
            if value == current.value:
                return True

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def _height(self, node: AVLNode | None) -> int:
        """Return the height of a node."""
        return 0 if not node else node.height

    def _update_height(self, node: AVLNode) -> None:
        """Update the stored height of a node."""
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node: AVLNode | None) -> int:
        """Return the balance factor of a node."""
        if not node:
            return 0

        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        """Perform a left rotation."""
        y = z.right
        subtree = y.left

        y.left = z
        z.right = subtree

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        """Perform a right rotation."""
        y = z.left
        subtree = y.right

        y.right = z
        z.left = subtree

        self._update_height(z)
        self._update_height(y)

        return y
