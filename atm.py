class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Deposit: {amount}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f'Withdraw: {amount}')
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Your balance is: {self.balance}")

    def print_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

def main():
    atm = ATM()

    while True:
        print("\nWelcome to the ATM!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == 3:
            atm.check_balance()
        elif choice == 4:
            atm.print_transactions()
        elif choice == 5:
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    main()
