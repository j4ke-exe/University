from PlaneQueue import PlaneQueue
from PlaneNode import PlaneNode

if __name__ == "__main__":
    plane_queue = PlaneQueue()
    
user_input = input()
tokens = user_input.split()

while tokens[0] != '-1':
	if tokens[0] == 'arriving':
		new_node = PlaneNode(tokens[1])
		plane_queue.push(new_node)
	elif tokens[0] == 'landed':
		popped_item = plane_queue.pop()
		print(popped_item, 'has landed.')
	plane_queue.print_queue()
	user_input = input()
	tokens = user_input.split()
