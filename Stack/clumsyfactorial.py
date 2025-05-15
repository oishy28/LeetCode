class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        
        op = ['*', '/', '+', '-']
        index = 0 

        for i in range(n-1, 0, -1):
            
                operation = op[index % 4]

                if operation == '*':
                    stack[-1] *= i
                elif operation == '/':
                    stack[-1] = int(stack[-1] / i)
                elif operation == '+':
                    stack.append(i)
                elif operation == '-':
                    stack.append(-i)
                
                index += 1

        return sum(stack)