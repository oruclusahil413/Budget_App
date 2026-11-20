class Account:
    def __init__(self,total_balance,transaction_history):
        self.total_balance = total_balance
        self.transaction_history = transaction_history

class MainAccount(Account):
    def __init__(self,total_balance,transaction_history,balance):
        super().__init__(total_balance,transaction_history)
        self.__balance=balance

class SavingsAccount(Account):
    def __init__(self,total_balance,transaction_history,balance):
        super().__init__(total_balance,transaction_history)
        self.__balance = balance
