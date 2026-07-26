
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    """A single node in a binary search tree."""

    value: int
    left: Node | None = None
    right: Node | None = None


class BinarySearchTree:
    """Binary search tree implementation for integer values."""

    def __init__(self) -> None:
        """Create an empty binary search tree."""
        self.root: Node | None = None

    def insert(self, value: int) -> None:
        """Insert a value into the binary search tree."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node | None, value: int) -> Node:
        """Insert a value starting from the given node."""
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value: int) -> Node | None:
        """Return Node if the value exists in the tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Node | None, value: int) -> Node | None:
        """Search for a value starting from the given node."""
        if not node or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def delete(self, value: int) -> Node | None:
        """Delete a value from the binary search tree if it exists."""
        self.root = self._delete_recursive(self.root, value)
        return self.root

    def _delete_recursive(self, node: Node | None, value: int) -> Node | None:
        """Delete a value starting from the given node."""
        if not node:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _find_min(self, node: Node) -> Node:
        """Find the node with the smallest value in a subtree."""
        current = node

        while current.left is not None:
            current = current.left

        return current
