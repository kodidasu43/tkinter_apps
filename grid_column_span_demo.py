from tkinter import *

window = Tk()

r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)


window.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# # def show_info():
    # # messagebox.showinfo("Information", "This is an informational message.")


# def custom_dialog():
    # dialog = tk.Toplevel()
    # dialog.title("Custom Dialog")
    # # Add widgets to the dialog
    # label = tk.Label(dialog, text="This is a custom dialog box.")
    # label.pack()
    # # Add buttons to control the dialog
    # ok_button = tk.Button(dialog, text="OK", command=dialog.destroy)
    # ok_button.pack()

# button = tk.Button(root, text="Show Info", command=custom_dialog)
# button.pack()

# root.mainloop()
