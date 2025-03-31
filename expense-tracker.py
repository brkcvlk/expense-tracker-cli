from cmd import Cmd
from command_list.add import Add_Expense
from command_list.update import Update_Expense
from command_list.delete import Delete_Expense
from command_list.list import List_Expenses
from command_list.summary import Summary_Expenses
from rich import print as pprint

count = 0
def Id():
    global count
    count += 1
    return count


class App(Cmd):

    Cmd.intro = pprint("[spring_green3]Welcome to the Expense Tracker CLI,After you see the text 'Starting..' you can type the commands[/spring_green3]")

    # Add a expense to list with description and amount
    def do_add(self, args):
        'usage : expense-tracker add <description>=str <amount>=int  description : Add a expense to list'
        if args:
            try:
                description = str(args.split()[0])
                amount = int(args.split()[1])
                Add_Expense(description=description,amount=amount,id=Id())
            except: 
                pprint("[bright_red]Please enter the arguments correctly, type 'help add' to see description[/bright_red]")
        else:
            pprint("[bright_red]Please enter the arguments[/bright_red]")
        

    # Update a expense in list with description,amount and id 
    def do_update(self, args):
        'usage : expense-tracker update <id>=int <description>=str <amount>=int description : Update a expense in list'
        if args:
            try:
                id = int(args.split()[0])
                description = str(args.split()[1])
                amount = int(args.split()[2])
                Update_Expense(id=id,description=description,amount=amount)
            except:
                pprint("[bright_red]Please enter the arguments correctly, type 'help update' to see description[/bright_red]")
        else:
            pprint("[bright_red]Please enter the arguments[/bright_red]")
    

    # Delete a expense from list with id
    def do_delete(self, args):
        'usage : expense-tracker delete <id>=int description : Delete a expense from list'
        if args:
            id = int(args.split()[0])
            Delete_Expense(id=id)
        else:
            pprint("[bright_red]Please enter an id to delete expense[/bright_red]")

    # View all expenses
    def do_list(self, args):
        'usage : expense-tracker list <optional:month> description : View all expenses'
        if args:
            month = int(args.split()[0])
            List_Expenses(month=month)
        else:
            List_Expenses(month=None)

    # View a summary of all expenses
    def do_summary(self, args):
        'usage : expense-tracker summary <optional:month> description : View a summary of all expenses'
        if args:
            month = int(args.split()[0])
            Summary_Expenses(month=month)
        else:
            Summary_Expenses(month=None)
    
    # Exit from app
    def do_exit(self, args):
        'usage : expense-tracker exit description : Exit from app '
        pprint("[dark_magenta]Exiting.. Goodbye :)[/dark_magenta]")
        raise SystemExit

if __name__ == "__main__":
    app = App()
    app.prompt = "expense-tracker "
    app.cmdloop(pprint("[spring_green3]Starting..[/spring_green3]"))