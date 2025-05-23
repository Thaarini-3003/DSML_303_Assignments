"""Functions Of Dictionary"""

# 1. Creating a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# 2. Creating a Dictionary (key:value -> value:number)
sam_marks = {"History": 88 , "Geography": 72 , "Mathematics": 97 ,"Physics": 78 , "Chemistry": 65 }
print(sam_marks)
print(sam_marks["Geography"])

# 3. Creating a Dictionary (key:value -> value:list)
dict2 = {'Ramesh':[150,46],'Suresh':[146,58],'Dinesh':[160,50]}
print(dict2["Suresh"])

# 4. Adding a single element to a Dict
dict2["Neeraj"] = [170,70]
print(dict2)

# 5. Adding multiple elements at once
dict2.update({"sunil":[100,99], "Disha": [88,94], "Rama": [66,55]})
print(dict2)

# 6. Deleting elements from Dict
del dict2["Suresh"]
print(dict2)

# 7. LENGTH of Dict
len = len(dict2)
print(len)

# 8. CLEAR : remove all entries from Dict
dict2.clear()
print(dict2)  # returns empty dict

# 9. DELETE : total Dictionary
del dict2
#print(dict2) # we cannot access d

# 10. POP()
sam_marks.pop("Physics")
print(sam_marks)

# 11. Popitem()
sam_marks.popitem()
print(sam_marks)
sam_marks.popitem()
sam_marks.popitem()
sam_marks.popitem()
print(sam_marks)
# sam_marks.popitem() # if dict is empty, we get KeyError

# 12. Keys()
print(thisdict.keys())
for k in thisdict.keys():
    print(k)

# 13. values()
print(thisdict.values())
for v in thisdict.values():
    print(v)

# 14. Copy()
dict1 = {1:"Mano", 2:"Jane", 3:"Catherine"}
dict2 = {"Mano": 100, "Jane": 200, "Catherine": 300}
dict1 = dict2.copy()
print(dict1)
# dict2.update({1:"Mano", 2:"Jane", 3:"Catherine"}) # Compile time error
# print(dict2)

# 15. Update
dict1.update(dict2)
print(dict1)

