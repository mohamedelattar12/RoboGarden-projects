import uuid

class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = str(uuid.uuid4())
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        with open(self.filename, 'w') as f:
            f.write("Transaction History:\n")
        print(f"Account created for {self.name} with account number {self.accountNumber}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            with open(self.filename, 'a') as f:
                f.write(f"Deposited: {amount}\n")
            print(f"{amount} deposited to {self.name}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            with open(self.filename, 'a') as f:
                f.write(f"Withdrawn: {amount}\n")
            print(f"{amount} withdrawn from {self.name}'s account.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance for {self.name} is {self.balance}.")
        return self.balance

    def get_account_number(self):
        return self.accountNumber

    def get_holder_name(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        with open(self.filename, 'r') as f:
            print(f.read())

# Test the BankAccount class with multiple operations

# Create a bank account
account1 = BankAccount("John Doe", "savings")

# Deposit money
account1.deposit(100)
account1.deposit(200)

# Withdraw money
account1.withdraw(50)
account1.withdraw(300)  # This should fail due to insufficient balance

# Check balance
account1.check_balance()

# Get account details
print("Account Number:", account1.get_account_number())
print("Holder Name:", account1.get_holder_name())
print("Account Type:", account1.get_account_type())

# Get transaction history
account1.get_transaction_history()
