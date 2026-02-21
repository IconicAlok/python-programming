# membership operator = used to test weather a value or variable is found in a sequence
#                       (string, list, tuples, set or dictionary)
#                       1. in
#                       2.not in

word = "APPLE"
# letter = input("Guess a letter form the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"There is no a {letter}")



# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")


students = {"Spongebob", "Patrick", "Sandy"}
#
# student = input("Enter a name of an student: ")
# if student in students:
#     print(f"{student} is a student ")
# else:
#     print(f"{student} was not found ")



grades = {"Sandy": "A",
          "Squidward":"B",
          "Spongebob": "C",
          "Patrick":"D"}

# student = input("Enter a name of a student: ")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}. ")
# else:
#     print(f"{student} was not found")

email = "alok@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Not valid email")