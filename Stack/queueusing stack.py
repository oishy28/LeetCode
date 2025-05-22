# # Queue using stack
# from collections import deque

# def queue_using_stack(stack1,x):
#     # Implementing queue using two stacks
#     # stack1 is used for enqueue operation
#     # stack2 is used for dequeue operation

#     stack2 = deque()
    
#     if stack1 is None:
#         return stack1.pop()
    
    
#     else:
#         stack2.append(x)
#         while stack1:
#             stack2.append(stack1.pop())
            
        
#         while stack2:
#             stack1.append(stack2.pop())
#         return stack1.
    
# if __name__ == "__main__":
#     stack1 = deque()
#     stack1.append(1)
#     stack1.append(2)
#     stack1.append(3)
#     x = 4
#     result = queue_using_stack(stack1,x)
#     print(result)
    

