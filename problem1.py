"""
Problem 1: Teque
"""


class Node:
    """
    Node class used as building block for linked list
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    """
    Class for representing a linked list, with different methods
    """

    def __init__(self):
        self.head = None

    def listprint(self):
        """Method that prints the linked list"""
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next

    def find_length(self):
        """Method that finds the length of linked list"""
        length = 0
        temp = self.head
        while temp != None:
            length += 1
            temp = temp.next
        return length

    def push_back(self, x):
        """Method that takes in a list-object
        from LinkedList-class, and an integer x,
        makes a node with value x and pushes it to the back of the list
        """
        new_node = Node(value=x)
        tail = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while tail.next is not None:
            tail = tail.next

        tail.next = new_node
        new_node.prev = tail

    def push_front(self, x):
        """Method that takes in a list-object
        from LinkedList-class, and an integer x,
        makes a node with value x and pushes it to the front of the list
        """
        new_node = Node(value=x)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def push_middle(self, x):
        """Method that takes in a list-object
        from LinkedList-class, and an integer x,
        makes a node with value x and pushes it to the middle of the list
        """
        length = self.find_length()
        new_node = Node(value=x)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None

        else:
            mid = (length // 2) if (length % 2 == 0) else ((length + 1) // 2)
            current = self.head
            for i in range(1, mid):
                current = current.next

            temp = current.next
            temp.prev = current

            current.next = new_node
            new_node.prev = current
            new_node.next = temp
            temp.prev = new_node






    def get(self, i):
        """Method that takes in an integer i, representing an index,
        and prints the value of the node at this given index
        """
        count = 0
        current = self.head
        while count != i:
            current = current.next
            count += 1
        print(current.value)


list1 = LinkedList()  # Make object of LinkedList class

# Lists to fill with given input, method and argument
functions = []
args = []

print("Input:")

N = int(input())  # Reading first line of input, stating number of input lines
for line in range(N):  # Reading input line by line
    function, arg = input().split()  # Splitting input lines in two
    functions.append(function)  # Appending to empty lists
    args.append(arg)

print("\nOutput:")
for function, arg in zip(functions, args):  # Looping through the lists
    getattr(list1, function)(int(arg))  # Calling given class method with given argument

#list1.listprint()
"""
Terminal > python3 problem1.py
Input:
9
push_back 9
push_front 3
push_middle 5
get 0
get 1
get 2
push_middle 1
get 1
get 2

Output:
3
5
9
5
1
"""
