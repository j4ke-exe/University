from PlaneList import PlaneList

class PlaneQueue:
    def __init__(self):
        self.plane_list = PlaneList()
        self.length = 0
    
    def push(self, new_node):
        # Insert as list tail (end of queue)
        self.plane_list.append(new_node)
        self.length = self.length +1

    def pop(self):
        # Copy data from list's head node (queue's front node)
        dequeued_item = self.plane_list.head.flight_code
                
        # Remove list head
        self.plane_list.remove_after(None)
        self.length = self.length -1
        
        # Return the dequeued item
        return dequeued_item

    def is_empty(self):
        return self.length == 0
        
    def print_queue(self):
        print('Air-traffic control queue')
        if not self.is_empty():
            print('   Next to land:', end=' ')
            cur_node = self.plane_list.head
            cur_node.print_node_data()
            print()
            
            if self.length > 1:
                print('   Arriving flights:')
                cur_node = cur_node.next
                while cur_node is not None:
                    print('      ', end='')
                    cur_node.print_node_data()
                    print()
                    cur_node = cur_node.next
        else:
            print('Queue is empty.')
        print()

# Input
# arriving AA213
# arriving DAL23
# arriving UA628
# landed
# -1
# Your output
# Air-traffic control queue
#    Next to land: AA213

# Air-traffic control queue
#    Next to land: AA213
#    Arriving flights:
#       DAL23

# Air-traffic control queue
#    Next to land: AA213
#    Arriving flights:
#       DAL23
#       UA628

# AA213 has landed.
# Air-traffic control queue
#    Next to land: DAL23
#    Arriving flights:
#       UA628
