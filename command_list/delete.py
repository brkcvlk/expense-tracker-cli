from . import data
import json
from rich import print as pprint

def Delete_Expense(id):
    global data
    for d in data:
        try:
            if d["id"] == id:
                data.remove(d)
                with open('expense.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    pprint(f"[bright_black]Expense deleted successfully (ID : {id})[/bright_black]")
            else:
                pprint("[bright_black]Trying to find...[/bright_black]")
        except:
            print("I couldn't find the expense. Please enter a correct id")