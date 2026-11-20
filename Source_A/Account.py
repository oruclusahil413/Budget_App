
class Account:
    def __init__(self,total_balance,transaction_history,loan_to_M,loan_to_Bank):
        self.total_balance = total_balance
        self.transaction_history = transaction_history
        self.loan_to_M = loan_to_M
        self.loan_to_Bank = loan_to_Bank

class MainAccount(Account):
    def __init__(self,total_balance,transaction_history,balance,loan_to_M,loan_to_Bank):
        super().__init__(total_balance,transaction_history,loan_to_M,loan_to_Bank)
        self.__balance=balance

class SavingsAccount(Account):
    def __init__(self,total_balance,transaction_history,balance,loan_to_M,loan_to_Bank):
        super().__init__(total_balance,transaction_history,loan_to_M,loan_to_Bank)
        self.__balance = balance
