"""
Change password frame
"""

from tkinter import messagebox, Frame
from GuiValues import GuiValues
import GlobalVariables as Globe


class ChangePassword(Frame):
    """Class for the change password frame"""

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)

        gv.set_password_button.config(command=self.set_password_pressed)

        # Place the labels and buttons
        gv.employee_number_label.place(x=200, y=100)
        gv.new_password_label.place(x=200, y=150)
        gv.confirm_password_label.place(x=200, y=200)
        gv.set_password_button.place(x=550, y=300)
        gv.cancel_button.place(x=550, y=375)
        gv.user_entry.place(x=400, y=100, width=gv.input_width)
        gv.set_password_entry.place(x=400, y=150, width=gv.input_width)
        gv.confirm_password_entry.place(x=400, y=200, width=gv.input_width)

        # Bind the enter key woo
        self.controller.bind('<Return>', lambda event: self.set_password_pressed())

    # Create method for logging in
    def set_password_pressed(self):
        """Method to check and change the password if it meets parameters"""
        employee_num = gv.name_var.get()
        password = gv.passw_var.get()
        confirmation = gv.confirm_passw_var.get()

        # Check to see if the user exists or if one was entered
        if not Globe.Pr.user_exists(employee_num):
            messagebox.showwarning("Doesn't Exist", "Employee Number Doesn't Exist!")

        # Make sure passwords are the same
        if employee_num == "":
            messagebox.showwarning("NO USER", "Please Enter an Employee Number!")
        elif password == "" or confirmation == "":
            messagebox.showwarning("Empty", "Please Enter a New Password!")
        elif password != confirmation:
            messagebox.showwarning("Unmatched", "Passwords do not match!")
        else:
            changed = Globe.Pr.change_password(employee_num, password)
            if not isinstance(changed, bool):
                if changed == "Fail":
                    messagebox.showerror("Password Not Strong Enough!",
                                         "Password has to have a minimum of:\n"
                                         "1 Upper Case Letter\n"
                                         "1 Special Character\n"
                                         "1 Special Number\n"
                                         "8 Characters Long")
            elif not changed:
                messagebox.showerror("Password Exists!",
                                     "Password exists! Please log in to change your password!")
            else:
                messagebox.showinfo("Success!", "Password Changed Successfully")
                self.controller.show_frame("LoginPage")

        gv.user_entry.delete(0, 'end')
        gv.set_password_entry.delete(0, 'end')
        gv.confirm_password_entry.delete(0, 'end')
