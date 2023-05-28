import tkinter as tk

class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, category, description, amount):
        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)

    def get_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    def get_expenses_by_category(self, category):
        category_expenses = [expense for expense in self.expenses if expense.category == category]
        return category_expenses

    def display_expenses(self):
        for expense in self.expenses:
            print(f"Date: {expense.date}, Category: {expense.category}, Description: {expense.description}, Amount: {expense.amount}")


def add_expense_button_clicked():
    date = date_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    amount = float(amount_entry.get())

    tracker.add_expense(date, category, description, amount)
    clear_entry_fields()


def clear_entry_fields():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


# Create the Expense Tracker instance
tracker = ExpenseTracker()

# Create the main window
window = tk.Tk()
window.title("Expense Tracker")

# Create labels and entry fields
date_label = tk.Label(window, text="Date:")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

category_label = tk.Label(window, text="Category:")
category_label.pack()
category_entry = tk.Entry(window)
category_entry.pack()

description_label = tk.Label(window, text="Description:")
description_label.pack()
description_entry = tk.Entry(window)
description_entry.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

# Create the "Add Expense" button
add_expense_button = tk.Button(window, text="Add Expense", command=add_expense_button_clicked)
add_expense_button.pack()

window.mainloop()
