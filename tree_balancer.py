import sys
from typing import List

def read_array() -> List[int]:
    """Reads an array where each int element is on its own line.
    """
    return [int(element) for element in sys.stdin.readlines()]

def order_array(arr: List[int]):
    """Orders an array such that it will be a balanced binary tree if inserted.
    """
    if len(arr) <= 2:
        return arr
    else:
        median_index = len(arr) // 2
        left_arr = order_array(arr[:median_index])
        right_arr = order_array(arr[median_index+1:])
        return [arr[median_index]] + left_arr + right_arr

def main():
    arr = read_array()
    ordered_arr = order_array(arr)
    for element in ordered_arr:
        print(element)

if __name__ == "__main__":
    main()
