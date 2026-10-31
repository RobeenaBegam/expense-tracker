import os

FILE_NAME = "expenses.txt"
expenses = []

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        for line in f:
            category, amount = line.strip().split(",")
            expenses.append((category, float(amount)))


def save_all():
    with open(FILE_NAME, "w") as f:
        for category, amount in expenses:
            f.write(category + "," + str(amount) + "\n")


while True:
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category (food, travel, etc.): ")
        amount = float(input("Enter amount: "))
        expenses.append((category, amount))
        save_all()
        print("Saved:", category, amount)
    elif choice == "2":
        total = 0
        print("Your expenses:")
        number = 1
        for category, amount in expenses:
            print(number, ".", category, "-", amount)
            total = total + amount
            number = number + 1
        print("Total:", total)
    elif choice == "3":
        number = int(input("Enter the number to delete: "))
        if 1 <= number <= len(expenses):
            expenses.pop(number - 1)
            save_all()
            print("Deleted")
        else:
            print("Invalid number")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")