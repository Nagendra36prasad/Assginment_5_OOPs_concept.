# Challenge 4: Implement a Banking Account
# Implement the basic structure of a parent class, "Account" and a child class, "SavingsAccount".
# Task1 --->Implement properties as instance variables, and set them to None or 0
#           Account has the following properties:
#           title
#           Balance
#           SavingsAccount has the following properties:
#           interestRate
# Task2 --->Create an initializer for Account class. The order of parameters should be the following, where Ashish is the title, and 5000 is the account balance:
#           Account("Ashish", 5000)
# Task3 --->Implement properties as instance variables, and set them to None or 0.
#          Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:
#          Account("Ashish", 5000, 5)
#          Here, Ashish is the title and 5000 is the balance and 5 is the interestRate.

class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.interestRate = interestRate


account = SavingsAccount("Ashish", 5000, 5)      # simple input
print("Name Of Savings Account Holder : ",account.title)
print("Balance Of Your Savings Account : ",account.balance)
print("Interestrate : ",account.interestRate,"%")

    