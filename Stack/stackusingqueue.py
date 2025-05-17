class MyStack:

    def __init__(self):
        self.val = []
        self.temp = []
        
        
        

    def push(self, x: int) -> None:
        self.temp.append(x)
        while self.val:
            self.temp.append(self.val.pop())
        while self.temp:
            self.val.append(self.temp.pop())
        
        

    def pop(self) -> int:
        if self.val:
            return self.val.pop()
        
        

    def top(self) -> int:
        return self.val[-1] if self.val else None

    def empty(self) -> bool:
        return len(self.val) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
