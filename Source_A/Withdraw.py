from Loan_Places import LoanPlaces
from Loan_Places import ManaTO
from Loan_Places import AzPulMat

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

        if self._amount_to_withdraw > account.total_balance:

            MissingAmountOfMoney=self.amount_to_withdraw-account.total_balance

            print("There is not enough money to withdraw")
            print(f"You are {MissingAmountOfMoney}$ short of wanted withdrawal amount")

            while True:
                print("Savings account(S) | Get loan (M) | Make negative (N)| Abandon (Q)")

                place_to_withdraw = input()
                if place_to_withdraw=="S" or place_to_withdraw=="M":

                    print(f"Do you want all withdrawal amount from M or S {self._amount_to_withdraw} (1)")
                    print(f"Or short amount of money only {MissingAmountOfMoney}$? (2)")
                    number_choice=int(input())
                    if number_choice==2:
                        self._amount_to_withdraw = MissingAmountOfMoney

                    elif place_to_withdraw=="M":

                        print("Take money from ManaTo(Manat) | AzPulMat(Azpul)")
                        loan_take_place=input()

                        if loan_take_place =="Manat":
                            manato=ManaTO([])
                            manato.take_loan(self.amount_to_withdraw,account)

                        elif loan_take_place =="AzPulMat":
                            azpul=AzPulMat([])
                            azpul.take_loan(self.amount_to_withdraw,account)
                else:
                    if place_to_withdraw=="Q":
                        return 0
                    elif place_to_withdraw=="N":

                        print("WARNING|if you make balance negative,bank will cut interest every day")
                        print("Abandon (Q)|Continue (C)")
                        choice=input()
                        if choice=="Q":
                            return 0
                        elif choice=="C":
                            return "Yaz"
                    elif place_to_withdraw=="S":
                        return "Yaz"

                    else:
                        print("Please enter valid choice")
