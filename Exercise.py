def shipping_label(*args, **kwargs): #keyword arguments follow positional otherwise syntax error
    for arg in args:
        print(arg, end=" ")
    print()
    # for key, value in kwargs.items():
    #     print(f"{key}:{value}")
    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")}")
        print(f"{kwargs.get("pobox")}")
    else:
        print(f"{kwargs.get("street")}")
    print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zip")}")

shipping_label("Dr.", "Spongebob","Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321"

               )