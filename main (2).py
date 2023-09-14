#write a program to create a instance of BankAccount class and test the deposit and withdrawal functionality.
class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number= account_number
    self.__account_holder_name= account_holder_name
    self.__account_balance= initial_balance
  def deposit (self,amount):
    if amount>0:
      self.__account_balance+= amount
      print("New balance: ₹.{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount.Please deposit a positive amount.")
  def withdraw(self,amount):
    if amount>0 and amount<= self.__account_balance:
      self.__account_balance= amount
      print("withdrawal ₹.{}. New balance: ₹.{}.".format(amount,self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("Account balance for {} (Account#{}): ₹.{}".forma(self.__account_holder_name,self.__account_number,self.__account_balance))

#crrate an instance of the class BankAccount.
account= BankAccount(account_number="123456789", account_holder_name="Gayathri.S", initial_balance=6000.0)

#test deposits and withdrawals functionality:
account.display_balance()
account.deposit(500.0)
amount.withdraw(200.0)
amount.withdraw(20000.0)
#account.display__balance()