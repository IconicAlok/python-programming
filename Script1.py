# if __name__==__main__ : (this script can be imported or run standalone).
#                          Function and class in module can be reused.
#                          Whithout the main block of code executing
# good practise (code is modular
#                help readability,
#                leaves no global variable
#                avoid un intended execution)
# ex. import library = import library for functionality
#                       when running library directly . display a help page


def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script 1")
    favorite_food("pizza")
    print("Good bye")

if __name__ == '__main__':
    main()