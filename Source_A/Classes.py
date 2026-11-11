class Category:

    def __init__(self,name):

        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=""):

        self.ledger.append({"amount":amount, "description": description})

    def withdraw(self,amount,description=""):

        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):

        return sum(item["amount"] for item in self.ledger)

    def transfer(self,amount,category):

        if self.check_funds(amount):
            self.withdraw(amount,description=f"Transfer to {category.name}")
            category.deposit(amount,description=f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self,amount):

        if amount<=self.get_balance():
            return True
        else:
            return False

    def __str__(self):

        title=self.name.center(30,"*")

        for item in self.ledger:

            description=item["description"][:23]
            mamount=f"{item['amount']:.2f}"

            total=f"Total: {self.get_balance()}"

            title+=f"\n{description:<23}{mamount:>7}"
            title+=total

