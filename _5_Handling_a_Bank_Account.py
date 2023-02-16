
# Challenge 5: Handling a Bank Account
# define methods for handling a bank account using concepts of inheritance.
# Task1 ---> In the Account class, implement the getBalance() method that returns balance.
# Task2 ---> In the Account class, implement the deposit(amount) method that adds amount to the balance.
#            It does not return anything.
# Task3 ---> In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.
#            It does not return anything.
# Task4 ---> In the SavingsAccount class, implement an interestAmount() method
#            that returns the interest amount of the current balance.

class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)          
        self.interestRate = interestRate / 100

    def interestAmount(self):
        return self.balance * self.interestRate

account = SavingsAccount("Ashish", 2000, 5)  # take a simple inuput # title = Avish , # balance = 2000 , interestRate = 5%
account.deposit(500)
print("Current Balance Of Your Savings Account Is:",account.getBalance())  # output: 2500
account.withdrawal(500)
print("Balance  After Withdrawal :",account.getBalance())  # output: 2000
print("Interest Amount",account.interestAmount())  # output: 100
