"""
Login Page
"""

from tkinter import messagebox
from GuiValues import *
import app


class LoginPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)

        # Place the labels and buttons
        gv.employee_number_label.place(x=200, y=100)
        gv.password_label.place(x=200, y=200)
        gv.login_button.place(x=550, y=300)
        gv.create_password_button.place(x=550, y=375)
        gv.user_entry.place(x=400, y=100, width=gv.inputWidth)
        gv.password_entry.place(x=400, y=200, width=gv.inputWidth)

        gv.login_button.config(command=self.login_pressed)

        self.controller.bind('<Return>', lambda event: self.login_pressed())

    # Create method for logging in
    def login_pressed(self):

        employee_num = gv.name_var.get()
        password = gv.passw_var.get()

        # Check to see if the user exists
        if not globe.pr.user_exists(employee_num):
            messagebox.showwarning("Doesn't Exist", "Employee Number Doesn't Exist!")

        # Create a warning if either field is blank
        if employee_num == "" or password == "":
            messagebox.showwarning("WARNING", "Employee Number or Password fields cannot be empty!")
        else:
            try:
                check = globe.pr.authenticate(employee_num, password)

                if check == 'None':
                    messagebox.showwarning("No Password!", "Please Reset Your Password")
                elif check:
                    # messagebox.showinfo("Success!", "Successfully Logged In")
                    self.controller.destroy()
                    globe.ud.access_check(employee_num)
                    app.App()
                else:
                    messagebox.showwarning("Error", "Employee Number or Password are Incorrect")
            except:
                messagebox.showerror("Error!", "Please Contact your Administrator to set your Password!")

        try:
            # Clear entry boxes
            gv.user_entry.delete(0, 'end')
            gv.password_entry.delete(0, 'end')
        except:
            print("Error but all is well ;)")
