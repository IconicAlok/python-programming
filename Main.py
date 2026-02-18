# 2D collections

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables  = ["celery", "carrot", "potatoes"]
# meats = ["chicken", "fish","turkey"]
#
# groceries = [fruits, vegetables, meats]

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrot", "potatoes"],
             ["chicken", "fish","turkey"]]


#
# print(groceries)
# print(groceries[0]) # fruits list
# print(groceries[1]) # vegetables list
# print(groceries[0][0]) # first item in fruits list
# print(groceries[0][1]) # Second item in fruits list
# print(groceries[0][2]) # Third item in fruits list
# # print(groceries[0][3]) # Error index out of range
# print(groceries[1][0]) # first item in vegetables list
# print(groceries[1][1]) # second item in vegetables list
# print(groceries[1][2]) # third item in vegetables list
# print(groceries[2][0]) # 1st item in meats list
# print(groceries[2][1]) # 2nd item in meats list
# print(groceries[2][2]) # 3rd item in meats list

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# list with tuples
groceries = [("apple", "orange", "banana", "coconut"),
             ("celery", "carrot", "potatoes"),
             ("chicken", "fish","turkey")]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# 2D tuples
groceries = (("apple", "orange", "banana", "coconut"),
             ("celery", "carrot", "potatoes"),
             ("chicken", "fish","turkey"))

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
# tuple made up with sets
groceries = {("apple", "orange", "banana", "coconut"),
             ("celery", "carrot", "potatoes"),
             ("chicken", "fish","turkey")}

