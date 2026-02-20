# *args         = allow you to pass multiple non-key arguments
# **kwargs      = allow you to pass multiple keyword-arguments
#                 1. Positional 2. default 3. keyword 4. ARBITRARY

# def add(a, b):
#     return a + b

# print(add(1,2, 3)) # error add() takes 2 positional arguments but 3 were given

def add(*args):
    # print(type(args)) # tuples
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3))
print(add(1,2,3,4))
print(add(1))