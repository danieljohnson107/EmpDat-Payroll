"""Class file for EditEmployee frame"""

from tkinter import messagebox, Frame, DISABLED
from GuiValues import GuiValues
import GlobalVariables as globe


class EditEmployee(Frame):
    """Class for the edit employee frame"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        # Change the command for the buttons
        gv.employees_button.config(command=lambda: self.clear_edit_employee("FindEmployee"))
        gv.payroll_button.config(command=lambda: self.clear_edit_employee("PayrollProcessing"))
        gv.my_profile_button.config(command=lambda: self.clear_edit_employee("MyProfile"))

        self.fill_values()

        # admin
        if globe.EMPACCESS == 1:
            # Disable Button

            # Disable Entry for self
            gv.emp_num_input.config(state=DISABLED)
            gv.pay_ytd_input.config(state=DISABLED)

            # Buttons
            gv.save_profile_button.place(x=740, y=50)
            # gv.refresh.place(x=0, y=80)
            # gv.refresh.config(command=None)

            # Define save profile button
            gv.save_profile_button.config(command=self.save_profile)

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
            gv.f_name_input.place(x=340, y=50,
                                  width=gv.input_width, height=gv.input_height)
            gv.l_name_input.place(x=340, y=75,
                                  width=gv.input_width, height=gv.input_height)
            gv.address_input.place(x=340, y=100,
                                   width=gv.input_width, height=gv.input_height)
            gv.address_two_input.place(x=340, y=125,
                                       width=gv.input_width,
                                       height=gv.input_height)
            gv.city_input.place(x=340, y=150,
                                width=gv.input_width, height=gv.input_height)
            gv.state_input.place(x=340, y=175,
                                 width=gv.input_width, height=gv.input_height)
            gv.zip_input.place(x=340, y=200,
                               width=gv.input_width, height=gv.input_height)
            gv.phone_input.place(x=340, y=225,
                                 width=gv.input_width, height=gv.input_height)
            gv.class_input.place(x=340, y=250,
                                 width=gv.input_width, height=gv.input_height)
            gv.emp_num_input.place(x=340, y=275,
                                   width=gv.input_width, height=gv.input_height)
            gv.password_input.place(x=340, y=300,
                                    width=gv.input_width, height=gv.input_height)
            gv.department_input.place(x=340, y=325,
                                      width=gv.input_width,
                                      height=gv.input_height)
            gv.pay_rate_input.place(x=340, y=350,
                                    width=gv.input_width, height=gv.input_height)
            gv.pay_ytd_input.place(x=340, y=375,
                                   width=gv.input_width, height=gv.input_height)
            gv.security_input.place(x=340, y=400,
                                    width=gv.input_width, height=gv.input_height)

        # general
        elif globe.EMPACCESS == 2:
            # Disable Button

            # Disable Entry Fields
            gv.f_name_input.config(state=DISABLED)
            gv.l_name_input.config(state=DISABLED)
            gv.class_input.config(state=DISABLED)
            gv.emp_num_input.config(state=DISABLED)
            gv.password_input.config(state=DISABLED)
            gv.pay_ytd_input.config(state=DISABLED)

            # Buttons
            gv.save_profile_button.place(x=0, y=40)

            # Define save profile button
            gv.save_profile_button.config(command=self.save_profile)

            # Labels
            gv.f_name_label.place(x=200, y=50)
            gv.l_name_label.place(x=200, y=75)
            gv.phone_label.place(x=200, y=100)
            gv.classification_label.place(x=200, y=125)
            gv.emp_number_label.place(x=200, y=150)
            gv.password_label_user.place(x=200, y=175)
            gv.department_label.place(x=200, y=200)
            gv.pay_rate_label.place(x=200, y=225)
            gv.pay_ytd_label.place(x=200, y=250)

            # Inputs
            gv.f_name_input.place(x=340, y=50,
                                  width=gv.input_width, height=gv.input_height)
            gv.l_name_input.place(x=340, y=75,
                                  width=gv.input_width, height=gv.input_height)
            gv.phone_input.place(x=340, y=100,
                                 width=gv.input_width, height=gv.input_height)
            gv.class_input.place(x=340, y=125,
                                 width=gv.input_width, height=gv.input_height)
            gv.emp_num_input.place(x=340, y=150,
                                   width=gv.input_width, height=gv.input_height)
            gv.password_input.place(x=340, y=175,
                                    width=gv.input_width, height=gv.input_height)
            gv.department_input.place(x=340, y=200,
                                      width=gv.input_width,
                                      height=gv.input_height)
            gv.pay_rate_input.place(x=340, y=225,
                                    width=gv.input_width, height=gv.input_height)
            gv.pay_ytd_input.place(x=340, y=250,
                                   width=gv.input_width, height=gv.input_height)

        # employee
        elif globe.EMPACCESS == 3:
            # Disable Button

            # Disable Entry Fields
            gv.f_name_input.config(state=DISABLED)
            gv.l_name_input.config(state=DISABLED)
            gv.phone_input.config(state=DISABLED)
            gv.department_input.config(state=DISABLED)

            # Buttons

            # Define save profile button

            # Labels
            gv.f_name_label.place(x=200, y=50)
            gv.l_name_label.place(x=200, y=75)
            gv.phone_label.place(x=200, y=100)
            gv.department_label.place(x=200, y=125)

            # Inputs
            gv.f_name_input.place(x=340, y=50,
                                  width=gv.input_width, height=gv.input_height)
            gv.l_name_input.place(x=340, y=75,
                                  width=gv.input_width, height=gv.input_height)
            gv.phone_input.place(x=340, y=100,
                                 width=gv.input_width, height=gv.input_height)
            gv.department_input.place(x=340, y=125,
                                      width=gv.input_width,
                                      height=gv.input_height)

        else:
            messagebox.showinfo("Error", "You do not have access. If you think you should,"
                                         " please contact your system administrator.")

    @staticmethod
    def save_profile():
        """Function to save the editted profile"""
        #Set the new values
        globe.Pr.save_profile(gv.emp_num_var.get(), gv.fname_var.get(), gv.lname_var.get(),
                              gv.address_var.get(), gv.address2_var.get(), gv.city_var.get(),
                              gv.state_var.get(), gv.zip_var.get(), gv.class_var.get(),
                              gv.pay_ytd_var.get(), gv.pay_rate_var.get(), gv.passw_var.get(),
                              gv.security_var.get(), gv.phone_var.get(), gv.department_var.get())

        # Pop up letting them know that it updated successfully
        messagebox.showinfo("Success!", "Successfully Updated")

    @staticmethod
    def fill_values():
        """Function to fill the edit employee page with values"""
        if globe.search_result != '':
            # Clear all fields in case of double click
            gv.f_name_input.delete(0, "end")
            gv.f_name_input.delete(0, "end")
            gv.l_name_input.delete(0, "end")
            gv.address_input.delete(0, "end")
            gv.address_two_input.delete(0, "end")
            gv.city_input.delete(0, "end")
            gv.state_input.delete(0, "end")
            gv.zip_input.delete(0, "end")
            gv.phone_input.delete(0, "end")
            gv.class_input.delete(0, "end")
            gv.emp_num_input.delete(0, "end")
            gv.password_input.delete(0, "end")
            gv.department_input.delete(0, "end")
            gv.pay_rate_input.delete(0, "end")
            gv.pay_ytd_input.delete(0, "end")
            gv.security_input.delete(0, "end")

            # Insert values from CSV
            gv.f_name_input.insert(0, globe.search_result[1])
            gv.l_name_input.insert(0, globe.search_result[2])
            gv.address_input.insert(0, globe.search_result[3])
            gv.address_two_input.insert(0, globe.search_result[4])
            gv.city_input.insert(0, globe.search_result[5])
            gv.state_input.insert(0, globe.search_result[6])
            gv.zip_input.insert(0, globe.search_result[7])
            gv.phone_input.insert(0, globe.search_result[14])
            gv.class_input.insert(0, globe.search_result[8])
            gv.emp_num_input.insert(0, globe.search_result[0])
            gv.password_input.insert(0, globe.search_result[12])
            gv.department_input.insert(0, globe.search_result[15])
            gv.pay_rate_input.insert(0, globe.search_result[11])
            gv.pay_ytd_input.insert(0, globe.search_result[9])
            gv.security_input.insert(0, globe.search_result[13])

    def clear_edit_employee(self, page_name):
        """Function to clear edit employee then change the page"""
        # Clear the search result value
        globe.search_result = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        # Clear the fields
        gv.f_name_input.delete(0, "end")
        gv.f_name_input.delete(0, "end")
        gv.l_name_input.delete(0, "end")
        gv.address_input.delete(0, "end")
        gv.address_two_input.delete(0, "end")
        gv.city_input.delete(0, "end")
        gv.state_input.delete(0, "end")
        gv.zip_input.delete(0, "end")
        gv.phone_input.delete(0, "end")
        gv.class_input.delete(0, "end")
        gv.emp_num_input.delete(0, "end")
        gv.password_input.delete(0, "end")
        gv.department_input.delete(0, "end")
        gv.pay_rate_input.delete(0, "end")
        gv.pay_ytd_input.delete(0, "end")
        gv.security_input.delete(0, "end")

        # Change the frame
        self.controller.show_frame(page_name)
