from Loan_Places import ManaTO, AzPulMat

class Withdraw:
    def __init__(self, amount_to_withdraw):
        self.amount_to_withdraw = amount_to_withdraw

    @property
    def amount_to_withdraw(self):
        return self._amount_to_withdraw

    @amount_to_withdraw.setter
    def amount_to_withdraw(self, withdrawing_value):
        if withdrawing_value <= 0:
            raise ValueError("Amount to withdraw must be greater than 0")
        self._amount_to_withdraw = withdrawing_value

    def withdraw_operation(self, account):

        if self._amount_to_withdraw > account.total_balance:
            missing_amount = self._amount_to_withdraw - account.total_balance

            print("There is not enough money to withdraw")
            print(f"You are {missing_amount}$ short of wanted withdrawal amount")

            while True:
                print("Savings account(S) | Get loan (M) | Make negative (N) | Abandon (Q)")
                place_to_withdraw = input().upper()

                if place_to_withdraw == "Q":
                    return 0

                elif place_to_withdraw in ("S", "M"):

                    print(f"Do you want all withdrawal amount from M or S {self._amount_to_withdraw}$ (1)")
                    print(f"Or short amount of money only {missing_amount}$? (2)")
                    number_choice = int(input())

                    loan_amount = self._amount_to_withdraw if number_choice == 1 else missing_amount

                    if place_to_withdraw == "M":
                        print("Take money from ManaTO(Manat) | AzPulMat(Azpul)")
                        loan_take_place = input()

                        if loan_take_place == "Manat":
                            manato = ManaTO()
                            manato.take_loan(loan_amount, account)
                        elif loan_take_place == "Azpul":
                            azpul = AzPulMat()
                            azpul.take_loan(loan_amount, account)
                        else:
                            print("Please enter valid loan place")
                            continue

                        account.total_balance -= self._amount_to_withdraw
                        return "Withdraw with loan completed"

                    elif place_to_withdraw == "S":
                        return "Yaz"

                elif place_to_withdraw == "N":
                    print("WARNING | If you make balance negative, bank will cut interest every day")
                    print("Abandon (Q) | Continue (C)")
                    choice = input().upper()
                    if choice == "Q":
                        return 0
                    elif choice == "C":
                        account.total_balance -= self._amount_to_withdraw
                        return "Negative balance applied"

                else:
                    print("Please enter valid choice")
        else:
            account.total_balance -= self._amount_to_withdraw
            return "Withdraw completed"