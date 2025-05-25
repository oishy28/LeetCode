class twostacks:
    def __init__(self,size):
        self.size = size
        self.arr = [None]* size
        self.top1 = -1
        self.top2 = size
        
    def push1(self,data):
        if self.top1 < self.top2 -1:
            self.top1 += 1
            self.arr[self.top1] = data
        else:
            print("Stack Overflow for Stack 1")
    
    def push2(self,data):
        if self.top2 > self.top1 + 1:
            self.top2 -=1
            self.arr[self.top2] = data
        else:
            print("Stack Overflow for Stack 2")
            
    def pop1(self):
        if self.top1 >= 0:
            data = self.arr[self.top1]
            self.top1 -= 1
            return data
        else:
            print("Stack Underflow for Stack 1")
            return None
    def pop2(self):
        if self.top2 < self.size:
            data = self.arr[self.top2]
            self.top2 += 1
            return data
        else:
            print("Stack Underflow for Stack 2")
            return None
        
        
if __name__ == "__main__":
    stack = twostacks(10)
    stack.push1(1)
    stack.push1(2)
    stack.push2(3)
    stack.push2(4)
    
    print("Popped from Stack 1:", stack.pop1())
    print("Popped from Stack 2:", stack.pop2())
    
    stack.push1(5)
    stack.push2(6)
    
    print("Popped from Stack 1:", stack.pop1())
    print("Popped from Stack 2:", stack.pop2())
    
    # Testing overflow
    for i in range(8):
        stack.push1(i + 8)  # This will cause overflow for Stack 1
        stack.push2(i + 8)  # This will cause overflow for Stack 2