from Node import Node
from LinkedList import LinkedList

if __name__ == "__main__":
    int_list = LinkedList()
    
    user_input = input()
    
    # Convert the string tokens into integers and insert into intList
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        new_node = Node(num)
        int_list.insert_in_ascending_order(new_node)
    
    int_list.print_list()
