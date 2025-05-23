"""Functions of Tuple"""

# 1. Creating a tuple using parentheses
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print(my_tuple)

# 2. Creating a tuple using the tuple() function
my_tuple = tuple([1, 2, 3, 'a', 'b', 'c'])
print(my_tuple)

# 3. Accessing the first element
print(my_tuple[0])

# 4. Accessing the fourth element
print(my_tuple[3])

# 5. SLICING: Accessing elements from index 1 to 3
print(my_tuple[1:4])  # Output: (2, 3, 'a')

# 6. COUNT:  the number of occurrences of 2
my_tuple1 = (1, 2, 3, 2, 4, 2)
count = my_tuple1.count(2)
print(count)  # Output: 3

# 7. INDEX: Finding the index of the first occurrence of 2
index = my_tuple1.index(2)
print(index)  # Output: 1

# 8. LEN : Finding the length of the tuple
length = len(my_tuple)
print(length)  # Output: 6

# 9. SORT : the elements of the tuple
my_tuple2 = (3, 1, 4, 2)
sorted_tuple = sorted(my_tuple2)
print(sorted_tuple)  # Output: (1, 2, 3, 4)

# 10. MIN : Finding the smallest element in the tuple
smallest = min(my_tuple2)
print(smallest)  # Output: 1

# 11. MAX : Finding the largest element in the tuple
largest = max(my_tuple2)
print(largest)  # Output: 4

# 12. Converting a list into a tuple
my_list = [1, 2, 3, 'a', 'b', 'c']
my_tuple_list = tuple(my_list)
print(my_tuple_list)  # Output: (1, 2, 3, 'a', 'b', 'c')

# 13. Concatenating two tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

# 14. Replicating a tuple three times
my_tuple = (1, 2, 3)
replicated_tuple = my_tuple * 3
print(replicated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 15. UPDATE TUPLE : Converting the tuple into a list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)

# Updating the list
my_list[1] = 4

# Converting the list back into a tuple
updated_tuple = tuple(my_list)
print(updated_tuple)  # Output: (1, 4, 3)


# 16. Deleting the tuple
del my_tuple
# Trying to access the tuple after deletion will raise an error
print(my_tuple)  # Output: NameError: name 'my_tuple' is not defined