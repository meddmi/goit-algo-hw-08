# goit-algo-hw-08

Algorithm homework project for working with binary search trees, AVL trees, and
heap-based greedy optimization.

## Description

The project contains two tree implementations:

- `BinarySearchTree` — a regular binary search tree.
- `AVLTree` — a self-balancing AVL tree.

Both trees support the following operations:

- inserting a value;
- searching for a value;
- deleting a value;
- finding the node with the smallest value;
- finding the node with the largest value;
- calculating the sum of all values in the tree.

The project also includes a heap-based algorithm for finding the cheapest order
to connect network cables.

## Tasks

### Task 1

Find the smallest value in a binary search tree or an AVL tree.

Implemented with:

- `BinarySearchTree.min()`
- `AVLTree.min()`

The demo also shows `max()` for finding the largest value.

### Task 2

Calculate the sum of all values in a binary search tree or an AVL tree.

Implemented with:

- `BinarySearchTree.sum()`
- `AVLTree.sum()`

### Task 3

Find the order for connecting network cables that minimizes the total connection
cost.

Each connection joins two cables, and its cost equals the sum of their lengths.
The optimal strategy is to always connect the two shortest cables first. The
project implements this strategy with Python's `heapq` min-heap in
`min_connection_cost()`.

## Files

- `binary_search_tree.py` — binary search tree implementation.
- `avl_tree.py` — AVL tree implementation.
- `main.py` — demo script that shows tree structure, minimum and maximum values,
  the sum of all tree values, and the optimal cable connection order.

## Run

```bash
python3 main.py
```

The demo creates a random set of 10 values from `1` to `50`, inserts them into
both the BST and AVL tree, and reuses those values as cable lengths. It prints:

- each tree structure;
- the minimum value;
- the maximum value;
- the sum of all tree values;
- the optimal cable connection order;
- the minimum total cable connection cost.
