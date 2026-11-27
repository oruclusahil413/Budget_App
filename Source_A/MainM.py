from Account import Account
from Account import MainAccount
from Account import SavingsAccount
from Withdraw import Withdraw

def CreateAccount():
     print("Write balance")
     balance=int(input())
     print("Savings account(S) | Daily-Usage account (A)")
     account_type=input()
     while True:
          if account_type=="S":
               return SavingsAccount(balance, [], balance, 0,0)
          elif account_type=="A":
               return MainAccount(balance, [], balance, 0,0)
          else:
               print("Account type error")


myaccount1 = CreateAccount()
print("İlkin balans:", myaccount1.total_balance)

w = Withdraw(100)
print(w.withdraw_operation(myaccount1))

print("Son balans:",myaccount1.total_balance)
print("Kredit borcu:",myaccount1.total_debts_loan)
print("Kredit siyahısı:",myaccount1.loan_list)