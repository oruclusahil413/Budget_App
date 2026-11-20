class Withdraw:
    def __init__(self,amount_to_withdraw):
        self._amount_to_withdraw = amount_to_withdraw

    @property
    def amount_to_withdraw(self):
        return self._amount_to_withdraw

    @amount_to_withdraw.setter
    def amount_to_withdraw(self,withdrawing_value):
        if withdrawing_value<=0:
            raise ValueError("Amount to withdraw must be greater than 0")
        else:
            self._amount_to_withdraw = withdrawing_value

    def withdraw_operation(self,account):
        if self._amount_to_withdraw<=_MainAccount.__total_balance:
            print("There is not enough money to withdraw")
            print("Savings account(S) | Get loan (M) | Make negative (N)| Abandon (Q)")

            place_to_withdraw = input()

            if place_to_withdraw=="Q":
                return 0
            elif place_to_withdraw=="M":