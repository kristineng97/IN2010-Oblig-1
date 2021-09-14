import sys
from typing import List
import heapq
from heapq import heapify, heappop, heappush
import math

def read_array() -> List[int]:
    """Reads an array where each int element is on its own line.
    """
    return [int(element) for element in sys.stdin.readlines()]

def balance_array(arr: List[int]):
    """Orders an array such that it will be a balanced binary tree if inserted.
    """
    if len(arr) <= 2:
        return arr
    else:
        median_index = (len(arr)) // 2
        right_arr = balance_array(arr[median_index+1:])
        left_arr = balance_array(arr[:median_index])
        return [arr[median_index]] + left_arr + right_arr



def balance_heap(heap):
    """Orders an array such that it will be a heap.
    """

    if len(heap) <= 2:
        for i in range(len(heap)):
            print(heappop(heap))
        return

    median_index = math.ceil(len(heap) / 2)
    left_heap = []
    for i in range(median_index-1):
        el = heappop(heap)
        heappush(left_heap, el)

    print(heappop(heap))

    balance_heap(heap)
    balance_heap(left_heap)


def main():
    arr = read_array()
    balanced_arr = balance_array(arr)
    for element in balanced_arr:
        print(element)

    heap = []
    for element in range(len(arr)):
        heappush(heap, arr[element])

    balance_heap(heap)



if __name__ == "__main__":
    main()
