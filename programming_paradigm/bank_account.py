class BankAccount:
    def __init__(self, account_balance = 0 ):
        
        self.account_balance = account_balance
        
    def deposit(self, amount):
        """deposits an amount into the account"""
        self.account_balance += amount

        return self.account_balance

    def withdraw(self, amount):
        """Withdraws money from the account balance and prints a result"""

        if self.account_balance >= amount:
          self.account_balance -= amount

          return self.account_balance

    def display_balance(self):
        return self.account_balance
