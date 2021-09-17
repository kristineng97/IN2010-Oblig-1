"""Triple ended queue implementation, with lists as the back-end data structure.
"""

class Teque:
    def __init__(self, capacity):
        self.left_list = [None] * (capacity + 1)
        self.right_list = [None] * (capacity + 1)

        self.front_ind = capacity // 2
        self.middle_front_ind = capacity // 2 + 1
        self.middle_back_ind = capacity // 2 - 1
        self.back_ind = capacity // 2

    @property
    def left_len(self):
        return self.middle_front_ind - self.front_ind - 1

    @property
    def right_len(self):
        return self.back_ind - self.middle_back_ind - 1

    def __len__(self):
        return self.left_len + self.right_len

    def __getitem__(self, i):
        if self.left_len > i:
            return self.left_list[self.front_ind + 1 + i]
        else:
            return self.right_list[self.middle_back_ind + 1 + i - self.left_len]

    def get(self, i):
        print(self[i])

    def push_front(self, value):
        self.left_list[self.front_ind] = value
        self.front_ind -= 1

        if len(self) % 2 == 0:
            self.shift_middle("left")

    def push_middle(self, value):
        self.left_list[self.middle_front_ind] = value
        self.middle_front_ind += 1

        if len(self) % 2 == 0:
            self.shift_middle("left")

    def push_back(self, value):
        self.right_list[self.back_ind] = value
        self.back_ind += 1

        if len(self) % 2 == 1:
            self.shift_middle("right")

    def shift_middle(self, direction):
        """Rebalance the lists by moving the middle element from one list to the other"""

        if direction == "left":
            if self.left_list[self.middle_front_ind] is None:
                self.right_list[self.middle_back_ind] = self.left_list[self.middle_front_ind - 1] 
                self.left_list[self.middle_front_ind - 1] = None
            else:
                self.right_list[self.middle_back_ind] = self.left_list[self.middle_front_ind] 
            
            self.middle_front_ind -= 1
            self.middle_back_ind -= 1

        elif direction == "right":
            if self.right_list[self.middle_back_ind] is None:
                self.left_list[self.middle_front_ind] = self.right_list[self.middle_back_ind + 1]
                self.right_list[self.middle_back_ind + 1] = None
            else:
                self.left_list[self.middle_front_ind] = self.right_list[self.middle_back_ind]
            
            self.middle_front_ind += 1
            self.middle_back_ind += 1

    def __str__(self):
        """Print out list, with the left part marked in red. Mainly for debugging"""
        left = self.left_list[self.front_ind+1:self.middle_front_ind]
        right = self.right_list[self.middle_back_ind+1:self.back_ind]
        print_list = [f"\033[91m{i}: {elem}\033[0m" for i, elem in enumerate(left)]
        print_list += [f"{i + self.left_len}: {elem}" for i, elem in enumerate(right)]

        return "\n".join(print_list)

def main():
    N = int(input())
    teque = Teque(N)

    for _ in range(N):
        function, arg = input().split()
        getattr(teque, function)(int(arg))

if __name__ == "__main__":
    main()
