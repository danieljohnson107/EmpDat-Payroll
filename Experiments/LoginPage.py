"""
Login Page
"""

from tkinter import *
from tkinter import messagebox
import main as m
from GuiValues import *


class LoginPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_buttons(self)

        # Place the labels and buttons
        gv.employee_number_label.place(x=200, y=100)
        gv.password_label.place(x=200, y=200)
        gv.login_button.place(x=550, y=300)
        gv.create_password_button.place(x=550, y=375)
        gv.user_entry.place(x=400, y=100, width=gv.inputWidth)
        gv.password_entry.place(x=400, y=200, width=gv.inputWidth)

        gv.login_button.config(command=self.login_pressed)

    # Create method for logging in
    def login_pressed(self):

        employee_num = gv.name_var.get()
        password = gv.passw_var.get()

        # Check to see if the user exists
        if not m.ud.user_exists(employee_num):
            messagebox.showwarning("Doesn't Exist", "Employee Number Doesn't Exist!")

        # Create a warning if either field is blank
        if employee_num == "" or password == "":
            messagebox.showwarning("WARNING", "Employee Number or Password fields cannot be empty!")
        else:
            check = m.ud.verify_user(employee_num, password)

            if check == 'None':
                messagebox.showwarning("No Password!",
                                       "Please Reset Your Password")
            elif check:
                # messagebox.showinfo("Success!", "Successfully Logged In")
                self.controller.show_frame("FindEmployee")
            else:
                messagebox.showwarning("Error", "Employee Number or Password are Incorrect")

        # Clear entry boxes
        gv.user_entry.delete(0, 'end')
        gv.password_entry.delete(0, 'end')
