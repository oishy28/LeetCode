#reverse linked list using stack

from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
def reverse_linked_list_using_stack(head):
    stack = deque()
    current = head
    
    # Push all nodes onto the stack
    while current:
        stack.append(current)
        current = current.next
        
    head = stack.pop()  # Pop the top node to be the new head
    current = head
    
    while stack:
        current.next = stack.pop()
        current = current.next
    current.next = None  # Set the next of the last node to None
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end ="")
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("Original Linked List:")
    print_linked_list(head)
    
    # Reverse the linked list using stack
    reversed_head = reverse_linked_list_using_stack(head)
    
    print("Reversed Linked List:")
    print_linked_list(reversed_head)
        

