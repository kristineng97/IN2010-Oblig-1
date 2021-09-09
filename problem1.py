

#Lage klasse
class Node:
   def __init__(self, value):
       self.value = value
       self.next = None
       self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method used for testing:
    def listprint(self):
        printval = self.head
        while printval is not None:
         print(printval.value)
         printval = printval.next

    def find_length(self):
        length = 0
        temp = self.head
        while (temp != None):
            length += 1
            temp = temp.next
        #self.length = length
        return length


    # The following methods takes in a list-object from LinkedList-class, and an integer x
    def push_back(self, x):
        new_node = Node(value = x)
        tail = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while (tail.next is not None):
                tail = tail.next

        tail.next = new_node
        new_node.prev = tail


    def push_front(self, x):
        new_node = Node(value = x)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def push_middle(self, x):
        new_node = Node(value = x)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.previous = None
            self.tail.next = None

        else:
            length = self.find_length()
            mid = (length // 2) if (length % 2 == 0) else ((length + 1)//2)
            current = self.head
            for i in range(1,mid):
                current = current.next

            temp = current.next
            temp.previous = current

            current.next = new_node
            new_node.previous = current
            new_node.next = temp
            temp.previous = new_node

        self.length += 1



    def get(self, i):
        count = 0
        current = self.head
        while (count != i):
            current = current.next
            count +=1
        print(current.value)
"""
list1 = LinkedList()
list1.push_back(10)
list1.push_front(9)
list1.push_front(7)
list1.push_front(6)
list1.push_middle(8)
function, arg = input().split()
print(getattr(list1, function)(int(arg)))

list1 = LinkedList()
list1.start = Node(10)
e2 = Node(9)
e3 = Node(11)

list1.start.next = e3

list1.start.prev = e2
list1.listprint()

list1 = LinkedList()

list1.push_back(10)
list1.push_front(9)
list1.push_front(7)
list1.push_front(6)
list1.push_middle(8)
list1.get(3)
list1.listprint()
"""
list1 = LinkedList()
list1.push_back(10)
list1.push_front(9)
list1.push_front(7)

N = int(input())

for line in range(N):
    function, arg = input().split()

    if getattr(list1, function) == list1.get:
        print(getattr(list1, function)(int(arg)))
    else:
        getattr(list1, function)(int(arg))
