class MainBank:
    def __init__(self, bank_name, commission_rate, interest_rate):
        self.commission_rate = commission_rate
        self.interest_rate = interest_rate

class Unibank(MainBank):
    def __init__(self, commission_rate, interest_rate, amount):
        super().__init__(commission_rate, interest_rate)
        self.amount = amount

class KapitalBank(MainBank):
    def __init__(self, commission_rate, interest_rate, amount):
        super().__init__(commission_rate, interest_rate)
        self.amount = amount

class ABB(MainBank):
    def __init__(self, commission_rate, interest_rate, amount):
        super().__init__(commission_rate, interest_rate)
        self.amount = amount

class PashaBank(MainBank):
    def __init__(self, commission_rate, interest_rate, amount):
        super().__init__(commission_rate, interest_rate)
        self.amount = amount