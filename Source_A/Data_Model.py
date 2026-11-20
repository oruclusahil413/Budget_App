class DataModel:
    def __init__(self,amount,description="",date,
                 op_type,category,transfer_number,tags):
        self.amount = amount
        self.description = description
        self.date = date
        self.op_type = op_type
        self.category = category
        self.transfer_number = transfer_number
        self.tags = tags


