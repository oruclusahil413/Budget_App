class LoanPlaces:
    def __init__(self,amount_to_loan,payment_interest,special_interest):
        self.amount_to_loan = amount_to_loan
        self.payment_interest = payment_interest

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
        return self.__payment_interest

    @special_interest.setter
    def special_interest(self,new_special_interest):
        if new_special_interest<0:
            raise ValueError("Special interest cannot be less than zero")
        else:
            self.__payment_interest = new_special_interest

class ManaTO(LoanPlaces):
    def __init__(self,amount_to_loan,payment_interest,special_interest):
        super().__init__(amount_to_loan,payment_interest,special_interest)
        self.special_interest = special_interest

class AzPulMat(LoanPlaces):
    def __init__(self,amount_to_loan,payment_interest,special_interest):
        super().__init__(amount_to_loan,payment_interest,special_interest)
