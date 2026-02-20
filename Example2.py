# return = statement used to end a function
#           and send a result back to the caller

def add(x, y):
    z = x + y
    return z
def subtract(x, y):
    z = x - y
    return z
def multiply(x, y):
    z = x * y
    return z
def divide (x, y):
    z = x / y
    return z

print(add(1,2))         # 3
print(subtract(1,2))    # -1
print(multiply(3,2))    # 6
print(divide(1,2))      # 0.5