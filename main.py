"""
Demonstrate tree algorithms and the optimal heap-based cable merge algorithm.

The script builds a binary search tree and an AVL tree from the same random
values, then shows their structure, minimum and maximum values, and total sum.
It also uses a min-heap to find the cheapest order for connecting cables.
"""

import heapq
from random import sample


from avl_tree import AVLNode, AVLTree
from binary_search_tree import Node, BinarySearchTree

TreeNode = Node | AVLNode


def node_value(node: Node | AVLNode | None) -> int | None:
    """Return the value stored in a tree node."""
    if node is None:
        return None

    return node.value


def fill_tree(tree: BinarySearchTree | AVLTree, values: list[int]) -> None:
    """Insert all demo values into a tree."""
    for value in values:
        tree.insert(value)


def print_separator() -> None:
    """Print a separator line for demo output."""
    print("-" * 30)


def show_min_max(tree: BinarySearchTree | AVLTree) -> None:
    """Print the minimum and maximum values found in a tree."""
    print(f"\n  Min value: {node_value(tree.min())}")
    print(f"  Max value: {node_value(tree.max())}")
    print_separator()


def print_tree(node: TreeNode | None, prefix: str = "", branch: str = "Root: ") -> None:
    """Print a tree sideways with the right subtree above the left subtree."""
    if node is None:
        print(f"    {prefix}{branch}empty")
        return

    print(f"    {prefix}{branch}{str(node.value)}")

    if node.left is not None:
        print_tree(node.left, f"{prefix}  ", "L-- ")

    if node.right is not None:
        print_tree(node.right, f"{prefix}  ", "R-- ")


def show_tree(tree: BinarySearchTree | AVLTree) -> None:
    """Print the visual structure of a tree."""
    print_separator()
    print("  Structure:")
    print_tree(tree.root)
    print_separator()


def min_connection_cost(cables: list[int]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Return the minimum total cost and merge order for connecting all cables.

    Each operation connects two cables and costs the sum of their lengths.
    The optimal strategy is to always connect the two shortest cables first.
    Each merge step is returned as a tuple: first cable, second cable, cost.
    """
    if len(cables) <= 1:
        return 0, []

    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0
    merge_order = []

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        connection_cost = first + second
        total_cost += connection_cost
        merge_order.append((first, second, connection_cost))

        heapq.heappush(heap, connection_cost)

    return total_cost, merge_order


def show_connection_order(cables: list[int]) -> None:
    """Print the optimal cable connection order and minimum total cost."""
    total_cost, merge_order = min_connection_cost(cables)

    if not merge_order:
        print("   No connections needed.")
        print(f"   Min cost: {total_cost}")
        return

    print("   Connect cables with length in order:")

    for step, (first, second, connection_cost) in enumerate(merge_order, start=1):
        print(f"    Step {step}: {first} & {second} -> connection cost: {connection_cost}")

    print(f"   Min cost: {total_cost}")


def main() -> None:
    """Run all tree and cable-connection demos."""
    values = sample(range(1, 51), 10)

    binary_search_tree = BinarySearchTree()
    avl_tree = AVLTree()

    fill_tree(binary_search_tree, values)
    fill_tree(avl_tree, values)

    print("\nTask 1:")
    print("  Binary search tree:")
    show_tree(binary_search_tree)
    show_min_max(binary_search_tree)
    print("\n\n  AVL tree:")
    show_tree(avl_tree)
    show_min_max(avl_tree)

    print("\nTask 2:")
    print("  Binary search tree:")
    print(f"    Sum: {binary_search_tree.sum()}")
    print("\n  AVL tree:")
    print(f"    Sum: {avl_tree.sum()}")
    print_separator()

    print("\nTask 3:")
    print(f"  For cables with values: {values}")
    show_connection_order(values)


if __name__ == "__main__":
    main()
