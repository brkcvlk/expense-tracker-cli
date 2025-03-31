from . import data
import json
from rich import print as pprint


def Update_Expense(id,description,amount):
    global data
    for d in data:
        try:
            if d["id"] == id:
                d["description"] = description
                d["amount"][1] = str(amount)
                with open('expense.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    pprint(f"[bright_black]Expense updated successfully (ID : {id})[/bright_black]")
                    return True
            else:
                pprint("[bright_black]Trying to find...[/bright_black]")
        except:
            print("[bright_red]I couldn't find the expense. Please enter a correct id[/bright_red]")