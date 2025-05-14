class BankAccount:
    def __init__(self, balance=0):  # default value of the attribute
        self.balance = balance  # setting value of the attribute

    # i.e. if value of balance is not set then it will be set to 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount  # adding amount to balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient fund!")
        self.balance -= amount
