# Iterables = An object/collection that can be return its element one at a time,
#             Allowing it to be iterated over in a loop


# numbers = [1, 2, 3, 4, 5]
numbers = (1,2,3,4,5)
fruits = {"Apple", "Orange", "Banana", "Coconut"}

# the name of the current element of out iterable should be
# descriptive for what iterating over
# for number in reversed(numbers):
#     print(number, end=" - ")

for num in numbers:
    print(num)


for fruit in fruits :
    print(fruit)


# for fruit in reversed(fruits):
#     print(fruit)
#     TypeError: 'set' object is not reversible

name = "Alok Kuri"

for character in name:
    print(character, end=" ")

print()


my_dictionary = {"A":1, "B":2, "C":3}

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} : {value}")