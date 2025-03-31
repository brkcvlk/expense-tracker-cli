from .modules import Expense
from . import data
import json
from rich import print as pprint

def Add_Expense(description, amount, id):
    global data
    data.append(Expense(description=description,amount=amount,id=id).__dict__)
    with open("expense.json", "w") as file:
        json.dump(data, file, indent=4)
    pprint(f"[bright_black]Expense added successfully (ID : {id})[/bright_black]")