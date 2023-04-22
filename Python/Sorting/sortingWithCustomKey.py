def key_is_name(element):
    return element[0]

def key_is_id(element):
    return element[1]
 
class_list = [("Robert", 135216), ("Amir", 612901), ("Jennifer", 194821), ("Ravi", 631104)]
name_result = sorted(class_list, key = key_is_name)
id_result = sorted(class_list, key = key_is_id)
print('Sort by name:', name_result)
print('Sort by id:', id_result)
 
# Sort by name: [('Amir', 612901), ('Jennifer', 194821), ('Ravi', 631104), ('Robert', 135216)]
# Sort by id: [('Robert', 135216), ('Jennifer', 194821), ('Amir', 612901), ('Ravi', 631104)]
