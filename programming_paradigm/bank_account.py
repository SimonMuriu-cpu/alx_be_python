class BankAccount:
  def __init__(self, account_balance, initial_balance=0):
    self.account_balance = account_balance
    self.initial_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.account_balance += amount

  def withdraw(self, amount):
    if self.account_balance >= amount > 0:
      self.account_balance -= amount
      return True
    return False

  def display_balance(self):
    return f"Current balance: ${self.account_balance:.2f}"