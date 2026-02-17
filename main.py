
# name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find("o")
# result = name.rfind("k")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit() # isdigit only return true when my string only digit
# result = name.isalpha() # isalpha return boolean true or false depending string only contained alphabet
# result = phone_number.count("-")
phone_number = phone_number.replace("-", " ")
print(phone_number)
