import random

# print(help(random))
high = 100
low = 1
options = ("rock","paper","scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","K","Q","A"]
# number = random.randint(low,high)
# number = random.random() # random method from random module will return floating point random number between 0 and 1.
# option = random.choice(options)
# print(option)
random.shuffle(cards)

print(cards)
