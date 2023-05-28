import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
window = tk.Tk()

# Create a Treeview widget
tree = ttk.Treeview(window)

# Define columns
tree["columns"] = ("Name", "Age", "City")

# Format columns
tree.column("#0", width=0, stretch=tk.NO)  # Hide the default first column
tree.column("Name", width=100)
tree.column("Age", width=50)
tree.column("City", width=100)

# Create column headings
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("City", text="City")

# Insert data rows
tree.insert("", tk.END, text="1", values=("John Doe", 30, "New York"))
tree.insert("", tk.END, text="2", values=("Jane Smith", 25, "London"))
tree.insert("", tk.END, text="3", values=("Alice Johnson", 35, "Paris"))

# Pack the Treeview widget
tree.pack()

# Start the Tkinter event loop
window.mainloop()
