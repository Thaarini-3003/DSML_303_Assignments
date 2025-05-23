"""Functions of List"""

# 1. Creating a List
mylist = ["apple", "banana", "cherry"]
print(mylist)

# 2. List allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# 3. List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# 4. Allow all datatypes
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#5. Find the datatype of List
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# 6. List constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# 7. Access the items in List
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# 8. Range of Index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# 9. Loop through the List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# 10. Loop through index number
thislist = ["apple", "banana", "cherry","watermelon"]
for i in range(len(thislist)):
  print(thislist[i])

# 11. Loop using While
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# 12. Loop using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# 13. Sorting a List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numlist = [100, 50, 65, 82, 23]
numlist.sort()
print(numlist)

# Sorting descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# 14. Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)






