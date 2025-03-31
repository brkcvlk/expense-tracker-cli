from . import data
from rich.table import Table
from rich.console import Console

def List_Expenses(month):
    global data
    if month == None:
        table = Table(title="Expenses")
        table.add_column("Id", justify='center', style="red")
        table.add_column("Date", justify="center")
        table.add_column("Description", style="cyan")
        table.add_column("Amount", justify="center", style="green")

        for d in data:
            table.add_row(f"{d['id']}", f"{d['date']}", f"{d['description']}", f"{''.join(d['amount'])}")
        
        console = Console()
        console.print(table)
    else:
        for d in data:
            if month ==  int(d["date"].split("/")[1]):
                table = Table(title="Expenses")
                table.add_column("Id", justify='center', style="red")
                table.add_column("Date", justify="center")
                table.add_column("Description", style="cyan")
                table.add_column("Amount", justify="center", style="green")

                table.add_row(f"{d['id']}", f"{d['date']}", f"{d['description']}", f"{''.join(d['amount'])}")
                
                console = Console()
                console.print(table)
            else:
                print(f"There is no expense in the {month}th month")
                