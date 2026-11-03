import json
import os

FILE_NAME = "bank.txt"
MINIMUM_BALANCE = 500


# Load account data
def load_accounts():
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error reading bank data.")
        return {}

# Save account data
def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


# Generate account number
def generate_account_number(accounts):
    if not accounts:
        return "1001"

    highest = max(int(number) for number in accounts)
    return str(highest + 1)


# Create account
def create_account(accounts):
    print("\n--- CREATE ACCOUNT ---")

    name = input("Enter customer name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        amount = float(input("Enter opening deposit: "))

        if amount < MINIMUM_BALANCE:
            print("Minimum opening deposit is Rs.500.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    account_number = generate_account_number(accounts)

    accounts[account_number] = {
        "name": name,
        "balance": amount
    }

    save_accounts(accounts)

    print("\nAccount created successfully!")
    print("Account Holder:", name)
    print("A/C No:", account_number)
    print("Balance:", amount)


# Deposit money
def deposit_money(accounts):
    print("\n--- DEPOSIT MONEY ---")

    number = input("Enter account number: ").strip()

    if number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    accounts[number]["balance"] += amount
    save_accounts(accounts)

    print("Deposit successful!")
    print("New Balance:", accounts[number]["balance"])


# Withdraw money
def withdraw_money(accounts):
    print("\n--- WITHDRAW MONEY ---")

    number = input("Enter account number: ").strip()

    if number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    balance = accounts[number]["balance"]

    if balance - amount < MINIMUM_BALANCE:
        print("Insufficient balance!")
        print("Minimum Rs.500 must remain.")
        return

    accounts[number]["balance"] -= amount
    save_accounts(accounts)

    print("Withdrawal successful!")
    print("Remaining Balance:", accounts[number]["balance"])


# Transfer money
def transfer_money(accounts):
    print("\n--- TRANSFER MONEY ---")

    sender = input("Enter sender account number: ").strip()
    receiver = input("Enter receiver account number: ").strip()

    if sender not in accounts:
        print("Sender account not found. Transfer cancelled.")
        return

    if receiver not in accounts:
        print("Account", receiver, "not found. Transfer cancelled.")
        return

    if sender == receiver:
        print("Cannot transfer to the same account.")
        return

    try:
        amount = float(input("Enter transfer amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    if accounts[sender]["balance"] - amount < MINIMUM_BALANCE:
        print("Insufficient balance!")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    save_accounts(accounts)

    print("Transfer successful!")
    print("Sender Balance:", accounts[sender]["balance"])
    print("Receiver Balance:", accounts[receiver]["balance"])


# Balance enquiry
def check_balance(accounts):
    print("\n--- BALANCE ENQUIRY ---")

    number = input("Enter account number: ").strip()

    if number not in accounts:
        print("Account not found.")
        return

    account = accounts[number]

    print("\nAccount Holder:", account["name"])
    print("Account Number:", number)
    print("Available Balance:", account["balance"])


# Main menu
def main():
    accounts = load_accounts()

    while True:
        print("\n================================")
        print("       SIMPLE BANKING SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Balance Enquiry")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            deposit_money(accounts)

        elif choice == "3":
            withdraw_money(accounts)

        elif choice == "4":
            transfer_money(accounts)

        elif choice == "5":
            check_balance(accounts)

        elif choice == "6":
            print("Thank you for using Simple Banking System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()