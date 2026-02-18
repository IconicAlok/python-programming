# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicate OK
#   Set = {} unordered and immutable, but Add/ Remove ok. N0 duplicates
# Tuple = () ordered and unchangeable, Duplicate OK, Faster

# fruits = ["apple","orange","banana","coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()

# print(fruits.index("apple"))
# print(fruits.index("coconut"))
# print(fruits.index("pineapple")) #error - cause not in the list

# print(fruits.count("banana"))
# print(fruits.count("pineapple"))


# print(fruits)

# for fruit in fruits:
#     print(fruit,end=" ")



"""
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

print(fruits[0:3])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit,end=" ")
"""
# set = {} unordered and immutable, but Add/ Remove ok. N0 duplicates

# fruits = {"apple", "orange", "banana", "coconut" }
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits[0]) # error 'set' object is not subscriptable

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits)



# tuples = () ordered and unchangeable, Duplicate OK, Faster

fruits = ("apple","orange","banana","coconut","coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
print(fruits.count("coconut"))

# print(fruits)
for fruit in fruits:
    print(fruit,end=" ")