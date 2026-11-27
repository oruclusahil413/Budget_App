from datetime import datetime

class LoanPlaces:

    def __init__(self, payment_interest=0.08, special_interest=0.06):
        self.payment_interest = payment_interest
        self.special_interest = special_interest

    @property

    def payment_interest(self):
        return self.__payment_interest

    @payment_interest.setter

    def payment_interest(self, new_payment_interest):
        if new_payment_interest < 0:
            raise ValueError("Payment interest cannot be less than zero")
        self.__payment_interest = new_payment_interest

    @property

    def special_interest(self):
        return self.__special_interest

    @special_interest.setter

    def special_interest(self, new_special_interest):
        if new_special_interest < 0:
            raise ValueError("Special interest cannot be less than zero")
        self.__special_interest = new_special_interest

    def take_loan(self, amount_to_loan, account, date_loan_taken=0):
        account.total_balance += amount_to_loan
        account.total_debts_loan += amount_to_loan

        if date_loan_taken == 0:
            date_loan_taken = datetime.now()

        loan_dictionary = {
            "PROVIDER": self.__class__.__name__,
            "DATE": date_loan_taken,
            "AMOUNT": amount_to_loan
        }
        account.loan_list.append(loan_dictionary)

        print("LOAN SUCCESSFULLY TAKEN")
        return loan_dictionary


class ManaTO(LoanPlaces):
    def __init__(self, payment_interest=0.06,
                 special_interest=0.09):
        super().__init__(payment_interest, special_interest)


class AzPulMat(LoanPlaces):
    def __init__(self, payment_interest=0.06,
                 special_interest=0.08):
        super().__init__(payment_interest, special_interest)