from Account import Account
from Loan_Places import ManaTO

def CreateAccount():
    account=Account(50,'Hello',0,0)
    return account
def GetLoan(myaccount1):
    manato=ManaTO([])
    loan=manato.take_loan(100,myaccount1)
    return manato

myaccount1=CreateAccount()
GetLoan(myaccount1)
print(LoanPlaces.see_debts(myaccount1))