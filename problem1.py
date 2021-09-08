N = int(input())

#Lage klasse

def push_back(list, x):
    list.back.next = newNode(x, prev = list.back)
    list.back = list.back.next

def push_front(list, x):
    list.front.prev = newNode(x, next = list.front)
    list.front = list.front.prev

def push_middle(list, x):


def get(list, i):



for line in range(N):
    function, arg = input().split()
    getattr(function)(?, int(arg))
