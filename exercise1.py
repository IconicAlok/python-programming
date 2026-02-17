# validate user input exercise
# 1. username no more than 12 character
# 2. username must not contain space
# 3. username must not contain digit

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 character")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("User name can't contain numbers")
else:
    print(f"Welcome {username}")