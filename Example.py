def display_name(*args):
    for arg in args:                            #unpacking arguments
        print(arg, end=" ")

display_name("Dr.","Spongebob", "Harold","Squarepants","III")
print()



# **kwargs
def print_address(**kwargs):
    # print(type(kwargs))                # dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake street",
              apt= "100",
              city="California",
              state="CF",
              zip="54321")
