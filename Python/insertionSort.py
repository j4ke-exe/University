def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        j = i

        # Insert num_list[i] into sorted part 
        # stopping once num_list[i] in correct position
        while j > 0 and num_list[j] < num_list[j - 1]:
            # Swap num_list[j] and num_list[j - 1]
            temp = num_list[j]
            num_list[j] = num_list[j - 1]
            num_list[j - 1] = temp
            j -= 1
    
# Create a list of unsorted values    
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Print unsorted list
print('UNSORTED:', numbers)

# Initial call to insertion_sort with index 
insertion_sort(numbers)

# Print sorted list
print('SORTED:', numbers)
