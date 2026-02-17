num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num > 10:
    print("Your number is not valid")
    num = int(input("Enter a number between 1 to 10: "))
print(f"Your number {num}")