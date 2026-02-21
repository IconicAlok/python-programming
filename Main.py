# list comprehension = A concise way to create lists in python
#                      Compact and easier to read and traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x * 2)
#
# print(doubles)

doubles = [x * 2 for x in range(1,11)]
triple = [y * 3 for y in range(1,11)]
square = [z * z for z in range(1,11)]

fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
fruits_char = [fruit[0] for fruit in ["apple", "orange", "banana", "coconut"]]

numbers = [1, -2, 3, -4, 5, -6, -7]
positive_num = [num for num in numbers if num>=0]
negative_num = [num for num in numbers if num<0]
even_num = [num for num in numbers if num % 2==0]
odd_num = [num for num in numbers if num % 2 == 1]
# print(odd_num)


grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade = [grade for grade in grades if grade >= 60]

print(passing_grade)