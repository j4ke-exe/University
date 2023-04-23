from Node import Node
from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)
    
    def pop(self):
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the popped item
        return popped_item

num_stack = Stack()
num_stack.push(45)
num_stack.push(56)
num_stack.push(11)

# Output stack
print('Stack after push:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

# Pop 11
popped_item = num_stack.pop()
print('Popped:', popped_item)

# Output final stack
print('Stack after pop:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print('\n')

# Stack after push: 11 56 45 
# Popped: 11
# Stack after pop: 56 45
