# Dictionaries =  a collections of {key : value} pairs
#                 ordered and changeable. No duplicates

capitals = {"Bangladesh": "Dhaka",
            "USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Bangladesh"))
# print(capitals.get("USA"))
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("Capital exist")
# else:
#     print("Capital doesn't exist")

# if capitals.get("Russia"):
#     print("Capital exists")
# else:
#     print("Capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# print(capitals)

# keys = capitals.keys() #technically keys is an object which resemble a list
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

item = capitals.items() # items returns a dictionary object which resembles 2d list tuple [(),(),()]
for key, value in capitals.items():
    print(f"{key}: {value}")