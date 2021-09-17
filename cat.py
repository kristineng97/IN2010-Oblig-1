"""Solution to problem 3.

Uses a list of ints to represent a tree, where each element is the index of the
parent.
"""

from typing import Tuple, List

def build_tree() -> Tuple[List[int], int]:
    """Builds a tree.

    Reads from stdin, assuming the first line is the node the cat is in, and the
    other lines have the parent node first, and then the children nodes.
    """
    tree = [-1]*101
    cat_node = int(input())
    line = input()
    while line != "-1":
        parent, *children = line.split()
        parent = int(parent)
        for child in children:
            tree[int(child)] = parent
        line = input()

    return tree, cat_node

def find_cat(tree: List[int], cat_node: int):
    """Finds the path from the cat to the root node, and prints it out.
    """
    current = cat_node
    while current != -1:
        print(current, end=" ")
        current = tree[current]
    print("")

def main():
    tree, cat_node = build_tree()
    find_cat(tree, cat_node)

if __name__ == "__main__":
    main()