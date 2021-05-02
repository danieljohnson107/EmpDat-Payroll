"""File for My Profile Frame"""

from tkinter import messagebox, DISABLED, Frame
from GuiValues import GuiValues
import GlobalVariables as Globe


class MyProfile(Frame):
    """Class for my profile frame"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        # fill the fields
        gv.my_profile_values()

        if Globe.EMPACCESS == 1:
            # Disable Button
            gv.my_profile_button.config(state=DISABLED)

            # Disable Entry for self
            gv.pay_rate_input.config(state=DISABLED)

            # Buttons
            gv.save_profile_button.place(x=740, y=50)

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

        elif Globe.EMPACCESS == 2:
            # Disable Button
            gv.my_profile_button.config(state=DISABLED)

            # Disable Entry Fields
            gv.f_name_input.config(state=DISABLED)
            gv.l_name_input.config(state=DISABLED)
            gv.class_input.config(state=DISABLED)
            gv.emp_num_input.config(state=DISABLED)
            gv.password_input.config(state=DISABLED)
            gv.pay_ytd_input.config(state=DISABLED)
            gv.security_input.config(state=DISABLED)
            gv.pay_rate_input.config(state=DISABLED)

            # Buttons
            gv.save_profile_button.place(x=0, y=40)

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

        elif Globe.EMPACCESS == 3:
            # Disable Button
            gv.my_profile_button.config(state=DISABLED)

            # Disable Entry Fields
            gv.class_input.config(state=DISABLED)
            gv.emp_num_input.config(state=DISABLED)
            gv.department_input.config(state=DISABLED)
            gv.pay_rate_input.config(state=DISABLED)
            gv.pay_ytd_input.config(state=DISABLED)
            gv.security_input.config(state=DISABLED)

            # Buttons
            gv.save_profile_button.place(x=0, y=40)

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
        else:
            messagebox.showinfo("Error", "You do not have access. "
                                         "If you think you should please contact your system administrator.")

    @staticmethod
    def save_profile():
        """Method to save the profile's data"""
        # Set the new values
        Globe.Pr.save_profile(gv.emp_num_var.get(), gv.fname_var.get(), gv.lname_var.get(), gv.address_var.get(),
                              gv.address2_var.get(), gv.city_var.get(), gv.state_var.get(), gv.zip_var.get(),
                              gv.class_var.get(), gv.pay_ytd_var.get(), gv.pay_rate_var.get(), gv.passw_var.get(),
                              gv.security_var.get(), gv.phone_var.get(), gv.department_var.get())

        # Pop up letting them know that it updated successfully
        messagebox.showinfo("Success!", "Successfully Updated")
