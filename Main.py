# Python banking program
# 1. Show balance
# 2. Diposite
# 3. Withdrow

def show_balance(balance):
    print("*******************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************")
def deposite():
    amount = float(input("Enter the amount to be deposited: "))

    if amount < 0 :
        print("Thats not a valid amount")
        return 0
    else:
        return amount
def withdrow(balance):
    print("*******************")
    amount = float(input("Enter the amount to be withdow: "))
    print("*******************")
    if amount < 0  :
        print("*******************")
        print("Invalid amount")
        print("*******************")
        return 0
    elif balance < amount:
        print("*******************")
        print("Insufficient funds.")
        print("*******************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("  Banking program  ")
        print("*******************")
        print("1.Show balance")
        print("2.Diposit")
        print("3.Whithdrow")
        print("4.Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposite()
        elif choice == "3":
            balance -= withdrow(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*******************")
            print("That is not a valid choice")
            print("*******************")

    print("*******************")
    print("Thank you! Have a nice day")
    print("*******************")

if __name__ == "__main__":
    main()