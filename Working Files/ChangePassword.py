"""
Chanage password pop up
"""

from tkinter import *
from tkinter import messagebox
from UserData import *
from GuiValues import *
import main as m

gv = GuiValues()


class ChangePassword(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Create entry variables
        self.name_var = StringVar()
        self.passw_var = StringVar()
        self.confirm_passw_var = StringVar()

        # Create the labels and buttons
        employee_number_label = Label(self, text="Employee Number", font=gv.fontProp)
        new_password_label = Label(self, text="New Password", font=gv.fontProp)
        confirm_password_label = Label(self, text="Confirm Password", font=gv.fontProp)

        set_password_button = Button(self, text="Set Password", width=gv.buttonWidth, height=gv.buttonHeight,
                                     bg=gv.buttonColor, fg=gv.buttonTextColor, font=gv.fontProp,
                                     command=lambda: self.set_password_pressed(controller))
        cancel_button = Button(self, text="Cancel", width=gv.buttonWidth, height=gv.buttonHeight, bg=gv.buttonColor,
                               fg=gv.buttonTextColor, font=gv.fontProp,
                               command=lambda: controller.show_frame("LoginPage"))

        self.user_entry = Entry(self, textvariable=self.name_var, font=gv.fontProp)
        self.set_password_entry = Entry(self, textvariable=self.passw_var, show="*", font=gv.fontProp)
        self.confirm_password_entry = Entry(self, textvariable=self.confirm_passw_var, show="*", font=gv.fontProp)

        # Place the labels and buttons
        employee_number_label.place(x=200, y=100)
        new_password_label.place(x=200, y=150)
        confirm_password_label.place(x=200, y=200)
        set_password_button.place(x=550, y=300)
        cancel_button.place(x=550, y=375)
        self.user_entry.place(x=400, y=100, width=gv.inputWidth)
        self.set_password_entry.place(x=400, y=150, width=gv.inputWidth)
        self.confirm_password_entry.place(x=400, y=200, width=gv.inputWidth)

    # Create method for logging in
    def set_password_pressed(self, controller):
        employee_num = self.name_var.get()
        password = self.passw_var.get()
        confirmation = self.confirm_passw_var.get()

        # Check to see if the user exists or if one was entered
        if not m.ud.user_exists(employee_num):
            messagebox.showwarning("Doesn't Exist", "Employee Number Doesn't Exist!")

        # Make sure passwords are the same
        if employee_num == "":
            messagebox.showwarning("NO USER", "Please Enter an Employee Number!")
        elif password == "" or confirmation == "":
            messagebox.showwarning("Empty", "Please Enter a New Password!")
        elif password != confirmation:
            messagebox.showwarning("Unmatched", "Passwords do not match!")
        else:
            m.ud.change_field(employee_num, password, 'password')
            messagebox.showinfo("Success!", "Password Changed Successfully")
            controller.show_frame("LoginPage")

        self.user_entry.delete(0, 'end')
        self.set_password_entry.delete(0, 'end')
        self.confirm_password_entry.delete(0, 'end')
