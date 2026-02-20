# keyword argument = an argument preceded by an identifier
#                    helps with readability
#                    order of argument doesn't matter
#                    1. Positional 2. default 3. KEYWORD 4. Arbitrary

def hello(greetings, title, first, last):
    print(f"{greetings} {title}{first} {last}")

hello("Hello",title="Mr. ",last="Squarepants" ,first="Spongebob")

hello("Hello",title="Mr.",last="John",first="James")

# positional arguments first then KEYWORD arguments otherwise error
