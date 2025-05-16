# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        
        def reverse(head):
            prev = None
            current = head 
            
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        head = reverse(head)
        
        max_val = head.val
        current = head
        
        while current and current.next:
            if current.next.val < max_val:
                current.next = current.next.next
            else:
                max_val = current.next.val
                current = current.next
                
