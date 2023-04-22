class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node
            
    # TODO: Write insert_in_ascending_order() method
    def insert_in_ascending_order(self, new_node):
        if self.head == None: # empty list
            self.head = new_node
            self.tail = new_node
        elif new_node.data <= self.head.data: # if new_node is smaller or equal to head
            self.prepend(new_node)
        elif new_node.data >= self.tail.data: # if new_node is larger or equal to tail
            self.append(new_node)
        else:
            current_node = self.head
            while (current_node.next != None) and (current_node.next.data < new_node.data):
                current_node = current_node.next
            self.insert_after(current_node, new_node)
   
    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node  
            if succeeding_node == None: # Remove last item
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None: # Remove tail
                self.tail = current_node

    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            cur_node.print_node_data()
            print(end=' ')
            cur_node = cur_node.next
            
# Input
# 8 3 6 2 5 9 4 1 7

# Output
# 1 2 3 4 5 6 7 8 9 
