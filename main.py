# conditional expression = A one line shortcut for if else statement (ternary operator)
#                           Print or assign a value vased on a condition
#                           x if condition else y

num = 5
a = 6
b = 7
age = 15
temperature = 20
user_role = "guest"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 ==0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited access"

print (result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)