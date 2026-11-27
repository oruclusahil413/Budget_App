class Account:
    def __init__(self, total_balance, transaction_history,
                 total_debts_loan, total_debts_bank):

        self.total_balance = total_balance
        self.loan_list = []
        self.transaction_history = transaction_history
        self.total_debts_loan = total_debts_loan
        self.total_debts_bank = total_debts_bank


class MainAccount(Account):
    def __init__(self, total_balance, transaction_history,
                          balance, total_debts_loan, total_debts_bank):

        super().__init__(total_balance, transaction_history,
                                  total_debts_loan, total_debts_bank)
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self,total_balance,transaction_history,
                          balance,total_debts_loan,total_debts_bank):

        super().__init__(total_balance, transaction_history,
                                 total_debts_loan, total_debts_bank)
        self.balance = balance