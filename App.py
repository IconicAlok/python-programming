# Variable is a container for value (string, integer, float, boolean)
#           a variable behaves as if it was the vaulue it contains

#Strings
first_name = "Alok"
food = "pizza"
email = "alok27@yahoo.com"

# Integers
age = 25
quantity = 3
num_of_student = 30

# Float
price = 10.99
gpa = 3.2
distance = 5.5

# Boolean
is_student = False
for_sale = False
is_online = False

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_student} students")

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} km")

print(f"Are you student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are online")
else:
    print("You are offline")