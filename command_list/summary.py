from . import data
import json
from rich import print as pprint

def Summary_Expenses(month):
    global data
    if month==None:
        with open("expense.json") as f:
            list = []
            GetData = json.load(f)
            for d in GetData:
                list.append(int(d["amount"][1]))
        
        pprint(f"[bright_black]Total expenses: ${sum(list)}[/bright_black]")     
    else:
        with open("expense.json") as f:
            list2 = []
            GetData2 = json.load(f)
            for d in GetData2:
                if month ==  int(d["date"].split("/")[1]):
                    list2.append(int(d["amount"][1]))
                else:
                    pprint(f"[bright_red]There is no total expense in the {month}th month[/bright_red]")
        pprint(f"[bright_black]Total expenses for {month}th month: ${sum(list2)}[/bright_black]")        