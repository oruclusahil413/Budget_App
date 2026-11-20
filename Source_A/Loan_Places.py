from datetime import datetime
class LoanPlaces:
    def __init__(self,amount_to_loan,payment_interest,special_interest,loan_list):
        self.amount_to_loan = amount_to_loan
        self.payment_interest = payment_interest
        self.special_interest = special_interest
        self.loan_list = []
        self.loan_dictionary = {}

    @property
    def payment_interest(self):
        return self.__payment_interest

    @payment_interest.setter
    def payment_interest(self,new_payment_interest):
        if new_payment_interest<0:
            raise ValueError("Payment interest cannot be less than zero")
        else:
            self.__payment_interest = new_payment_interest

    @property
    def special_interest(self):
        return self.__special_interest

    @special_interest.setter
    def special_interest(self,new_special_interest):
        if new_special_interest<0:
            raise ValueError("Special interest cannot be less than zero")
        else:
            self.__special_interest = new_special_interest

    def take_loan(self,amount_to_loan,account,date_loan_taken=0):
        total_debt=0
        loan_taken=amount_to_loan
        account.total_balance=account.total_balance+loan_taken

        if date_loan_taken !=0:
           date_loan_taken=date_loan_taken
        else:
            date_loan_taken=datetime.now()

        loan_dictionary={"DATE":date_loan_taken,
                         "AMOUNT":amount_to_loan}

        self.loan_list.append(loan_dictionary)

        return ("LOAN SUCCESFULLY TAKEN")

class ManaTO(LoanPlaces):
    def __init__(self,amount_to_loan,payment_interest,special_interest,loan_list):
        super().__init__(amount_to_loan,payment_interest,special_interest,loan_list)

class AzPulMat(LoanPlaces):
    def __init__(self,amount_to_loan,payment_interest,special_interest,loan_list):
        super().__init__(amount_to_loan,payment_interest,special_interest,loan_list)
