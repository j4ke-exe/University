class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        
    def print_node_data(self):
        print(self.data, end='')
