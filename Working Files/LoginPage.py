"""
Login Page
"""

from tkinter import *
from tkinter import messagebox
import main as m
from GuiValues import *

gv = GuiValues()


class LoginPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Create entry variables
        self.name_var = StringVar()
        self.passw_var = StringVar()

        # Create the labels and buttons
        employee_number_label = Label(self, text="Employee Number",
                                      font=gv.fontProp)
        password_label = Label(self, text="Password", font=gv.fontProp)

        login_button = Button(self, text="Login", width=gv.buttonWidth,
                              height=gv.buttonHeight, bg=gv.buttonColor,
                              fg=gv.buttonTextColor, font=gv.fontProp,
                              command=self.login_pressed)
        create_password_button = Button(self, text="Don't Have a Password?",
                                        width=gv.buttonWidth,
                                        height=gv.buttonHeight,
                                        bg=gv.buttonColor,
                                        fg=gv.buttonTextColor,
                                        font=gv.fontProp,
                                        command=lambda: controller.show_frame("ChangePassword"))

        self.user_entry = Entry(self, textvariable=self.name_var,
                                font=gv.fontProp)
        self.password_entry = Entry(self, textvariable=self.passw_var,
                                    show="*", font=gv.fontProp)

        # Place the labels and buttons
        employee_number_label.place(x=200, y=100)
        password_label.place(x=200, y=200)
        login_button.place(x=550, y=300)
        create_password_button.place(x=550, y=375)
        self.user_entry.place(x=400, y=100, width=gv.inputWidth)
        self.password_entry.place(x=400, y=200, width=gv.inputWidth)

    # Create method for logging in
    def login_pressed(self):

        employee_num = self.name_var.get()
        password = self.passw_var.get()

        # Check to see if the user exists
        if not m.ud.user_exists(employee_num):
            messagebox.showwarning("Doesn't Exist",
                                   "Employee Number Doesn't Exist!")

        # Create a warning if either field is blank
        if employee_num == "" or password == "":
            messagebox.showwarning("WARNING", "Employee Number or Password fields cannot be empty!")
        else:
            check = m.ud.verify_user(employee_num, password)

            if check == 'None':
                messagebox.showwarning("No Password!",
                                       "Please Reset Your Password")
            elif check:
                messagebox.showinfo("Success!", "Successfully Logged In")
                self.controller.show_frame("FindEmployee")
            else:
                messagebox.showwarning("Error", "Employee Number or Password are Incorrect")

        # Clear entry boxes
        self.user_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
