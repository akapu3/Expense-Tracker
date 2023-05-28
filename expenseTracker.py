import string
import csv
import tkinter as tk


expenses = [] # Contains all the expenses


class Expense:
    def __init__(self,name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __str__(self):
        return self.name + ": " + self.category + " - " + str(self.amount)

    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getAmount(self):
        return float(self.amount)

def main():
    loadexpenses()
    i = ""
    while not i.__eq__("E"):
        i = input("Enter A to add Expense, B to display current expenses, C to sort by Category, D to sort by amount, E to exit, F for total expenses: ")
        if i.__eq__("A"):
            name = input("Enter Name: ")
            category = input("Enter Category: ")
            amount = input("Enter Amount: ")
            expenses.append(Expense(name, category, float(amount)))
        elif i.__eq__("B"):
            printexpenses(expenses)
        elif i.__eq__("C"):
            category = input("Enter Category: ")
            x = sortbycategory(category)
            printexpenses(x)
        elif i.__eq__("D"):
            x = sortbyamount()
            printexpenses(x)
        elif i.__eq__("F"):
            print("Total Expense = " + str(get_total_expenses()))
    saveexpenses()

##Seperate Each option in main into a function
#Then continue setting up the window
#Each button should lead to a pop out window where the use can log their expense



def add_expense_button_clicked():
    date = add_expense_entry.get()
    category = category_entry.get()
    amount = float(amount_entry.get())

   ## addexpense(date, category, amount)
    clear_entry_fields()


def clear_entry_fields():
    add_expense_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def saveexpenses():
    with open("expenses.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for elements in expenses:
            writer.writerow([elements])

def loadexpenses():
    with open("expenses.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x = ''.join(row)
            y = x.index(":")
            z = x.index("-")
            expenses.append(Expense(x[:y],x[y+2:z-1],x[z+2:]))


def sortbycategory(category):
    current = []
    for i in expenses:
        x = i.getCategory()
        if x.__eq__(category):
            current.append(i)

    return current


def sortbyamount():
    d = input("A for greater than, B for less than, C for the largest expense, D for the smallest expense: ")
    current = []
    if d.__eq__("A"):
        amount = float(input("Enter Amount: "))
        for i in expenses:
            x = i.getAmount()
            if x > amount:
                current.append(i)
    elif d.__eq__("B"):
        amount = float(input("Enter Amount: "))
        for i in expenses:
            x = i.getAmount()
            if x < amount:
                current.append(i)
    elif d.__eq__("C"):
        largest = Expense(None,None,0)
        for i in expenses:
            x = i.getAmount()
            if x > largest.getAmount():
                largest = i
        current.append(largest)
    elif d.__eq__("D"):
        smallest = Expense(None,None,18446744073709551615)
        for i in expenses:
            x = i.getAmount()
            if x < smallest.getAmount():
                smallest = i
        current.append(smallest)
    else:
        print("Invalid input")
        return
    return current

def printexpenses(list):
    for i in list:
        print(i)

def get_total_expenses():
        sum = 0
        for i in expenses:
            sum += i.getAmount()
        return sum

    window = tk.Tk()
    window.title("Expense Tracker")
    window.geometry("1000x600")  # Width: 400 pixels, Height: 300 pixels

    add_expense_label = tk.Label(window, text="Add Expense:")
    add_expense_label.pack()
    add_expense_entry = tk.Entry(window)
    add_expense_entry.pack()

    category_label = tk.Label(window, text="Category:")
    category_label.pack()
    category_entry = tk.Entry(window)
    category_entry.pack()

    amount_label = tk.Label(window, text="Amount:")
    amount_label.pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()


    window.mainloop()





main()

# sort by category
# sort by most expensive
# Budget feature - add budget, display remaining budget, display a piechart in the gui?

