import datetime

class Expense:
    def __init__(self, description, amount, id):
        self.description = description
        self.amount = ["$",str(amount)]
        self.id = id
        self.date = str(datetime.datetime.now().strftime("%d/%m/%Y"))