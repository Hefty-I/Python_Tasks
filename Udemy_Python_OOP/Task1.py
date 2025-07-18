class Bank:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds")

# Create two instances of the Bank class
p1 = Bank()
p2 = Bank()

# Set details for both accounts
p1.set_details("Alice Johnson")  # Using default balance of 0
p2.set_details("Bob Smith") 

# Display initial account details
print("Initial Account Details:")
p1.display()
p2.display()

print("-------------------------")
# Perform transactions on first account
p1.deposit(1000)
p1.withdraw(200)
print("\nAfter transaction account detail:")
p1.display()

print()

# Perform transactions on second account
p2.deposit(300)
p2.withdraw(100)
p2.withdraw(1000)  # This should show insufficient funds
print("\nAfter transaction account detail:")
p2.display()
