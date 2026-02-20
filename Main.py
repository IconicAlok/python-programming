# default arguments = A default value for certain parameter
#                     default is used when that argument is omitted
#                     make your function more flexible, reduce # of argument
#                     1. Positional 2. DEFAULT 3. Arbitrary

def net_price(list_price, discount = 0.0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500,0,0.05))
# print(net_price(500))
# print(net_price(500, 0.1))
print(net_price(500, 0.1, 0.0))