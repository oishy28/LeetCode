class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def Remove_Middle(s):
    stack1 = Stack()
    n = len(s)
    middle_index = n // 2

    # Push all elements except the middle into stack1
    for i in range(n-1,-1, -1):
        if i != middle_index:
            stack1.push(s[i])
            
        

    return stack1.items


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    result = Remove_Middle(s)
    print(result)
