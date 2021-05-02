import tkinter.messagebox
from tkinter import Frame, DISABLED
from GuiValues import GuiValues
import GlobalVariables as Globe


class EnterNewEmployee(Frame):
    """New Employee Manual Entry frame"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        # Disable buttons
        gv.employees_button.config(state=DISABLED)
        gv.new_employee_button.config(state=DISABLED)

        # Place Buttons
        gv.new_employee_button.place(x=0, y=40)
        gv.find_employee_button.place(x=0, y=80)
        gv.import_employee_button.place(x=0, y=120)
        gv.save_profile_button.place(x=740, y=50)

        # assign the proper stuff to the thing
        gv.save_profile_button.config(command=self.save)

        # Labels
        gv.f_name_label.place(x=200, y=50)
        gv.l_name_label.place(x=200, y=75)
        gv.address_label.place(x=200, y=100)
        gv.address_line_two_label.place(x=200, y=125)
        gv.city_label.place(x=200, y=150)
        gv.state_label.place(x=200, y=175)
        gv.zip_code_label.place(x=200, y=200)
        gv.phone_label.place(x=200, y=225)
        gv.classification_label.place(x=200, y=250)
        gv.emp_number_label.place(x=200, y=275)
        gv.password_label_user.place(x=200, y=300)
        gv.department_label.place(x=200, y=325)
        gv.pay_rate_label.place(x=200, y=350)
        gv.pay_ytd_label.place(x=200, y=375)
        gv.security_access_label.place(x=200, y=400)

        # Inputs
        gv.f_name_input.place(x=340, y=50, width=gv.input_width, height=gv.input_height)
        gv.l_name_input.place(x=340, y=75, width=gv.input_width, height=gv.input_height)
        gv.address_input.place(x=340, y=100, width=gv.input_width, height=gv.input_height)
        gv.address_two_input.place(x=340, y=125, width=gv.input_width, height=gv.input_height)
        gv.city_input.place(x=340, y=150, width=gv.input_width, height=gv.input_height)
        gv.state_input.place(x=340, y=175, width=gv.input_width, height=gv.input_height)
        gv.zip_input.place(x=340, y=200, width=gv.input_width, height=gv.input_height)
        gv.phone_input.place(x=340, y=225, width=gv.input_width, height=gv.input_height)
        gv.class_input.place(x=340, y=250, width=gv.input_width, height=gv.input_height)
        gv.emp_num_input.place(x=340, y=275, width=gv.input_width, height=gv.input_height)
        gv.password_input.place(x=340, y=300, width=gv.input_width, height=gv.input_height)
        gv.department_input.place(x=340, y=325, width=gv.input_width, height=gv.input_height)
        gv.pay_rate_input.place(x=340, y=350, width=gv.input_width, height=gv.input_height)
        gv.pay_ytd_input.place(x=340, y=375, width=gv.input_width, height=gv.input_height)
        gv.security_input.place(x=340, y=400, width=gv.input_width, height=gv.input_height)

    @staticmethod
    def save():
        """Method to save the new employee to the DB"""
        try:
            Globe.Pr.new_user(gv.emp_num_var.get(), gv.fname_var.get(), gv.lname_var.get(),
                              gv.address_var.get(), gv.address2_var.get(), gv.city_var.get(),
                              gv.state_var.get(), gv.zip_var.get(), gv.class_var.get(),
                              gv.pay_ytd_var.get(), gv.pay_rate_var.get(), gv.passw_var.get(),
                              gv.security_var.get(), gv.phone_var.get(), gv.department_var.get())
            tkinter.messagebox.showinfo("Success!", "User was successfully added to database!")
        except:
            tkinter.messagebox.showerror("Not Added!", "The user could not be add to the database!\n"
                                                       "Check your values then try again.")
