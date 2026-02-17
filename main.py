# indexing = accessing element of sequence [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[1])
# print(credit_number[: 4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[: : 3])

last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

credit_number = credit_number[ : : -1] # reverse the string
print(credit_number)