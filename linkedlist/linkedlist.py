class node:
    def __init__(self,data= None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()
        
    def insert(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count +=1
            cur = cur.next
        return count
    
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)