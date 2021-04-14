from GuiValues import *
import GlobalVariables as globe


class EditEmployee(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        gv.edit_profile_values()

        # admin
        if globe.emp_access == 1:
            # Disable Button

            # Disable Entry for self
            gv.empNumInput.config(state=DISABLED)
            gv.payYTDInput.config(state=DISABLED)

            # Buttons
            gv.saveProfileButton.place(x=0, y=40)

            # Define save profile button
            gv.saveProfileButton.config(command=self.save_profile)

            # Labels
            gv.fNameLabel.place(x=200, y=50)
            gv.lNameLabel.place(x=200, y=75)
            gv.addressLabel.place(x=200, y=100)
            gv.addressLineTwoLabel.place(x=200, y=125)
            gv.cityLabel.place(x=200, y=150)
            gv.stateLabel.place(x=200, y=175)
            gv.zipCodeLabel.place(x=200, y=200)
            gv.phoneLabel.place(x=200, y=225)
            gv.classificationLabel.place(x=200, y=250)
            gv.empNumberLabel.place(x=200, y=275)
            gv.passwordLabel.place(x=200, y=300)
            gv.departmentLabel.place(x=200, y=325)
            gv.payRateLabel.place(x=200, y=350)
            gv.payYTDLabel.place(x=200, y=375)
            gv.securityAccessLabel.place(x=200, y=400)

            # Inputs
            gv.fNameInput.place(x=340, y=50,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.lNameInput.place(x=340, y=75,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.addressInput.place(x=340, y=100,
                                  width=gv.inputWidth, height=gv.inputHeight)
            gv.addressTwoInput.place(x=340, y=125,
                                     width=gv.inputWidth,
                                     height=gv.inputHeight)
            gv.cityInput.place(x=340, y=150,
                               width=gv.inputWidth, height=gv.inputHeight)
            gv.stateInput.place(x=340, y=175,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.zipInput.place(x=340, y=200,
                              width=gv.inputWidth, height=gv.inputHeight)
            gv.phoneInput.place(x=340, y=225,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.classInput.place(x=340, y=250,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.empNumInput.place(x=340, y=275,
                                 width=gv.inputWidth, height=gv.inputHeight)
            gv.passwordInput.place(x=340, y=300,
                                   width=gv.inputWidth, height=gv.inputHeight)
            gv.departmentInput.place(x=340, y=325,
                                     width=gv.inputWidth,
                                     height=gv.inputHeight)
            gv.payRateInput.place(x=340, y=350,
                                  width=gv.inputWidth, height=gv.inputHeight)
            gv.payYTDInput.place(x=340, y=375,
                                 width=gv.inputWidth, height=gv.inputHeight)
            gv.securityInput.place(x=340, y=400,
                                   width=gv.inputWidth, height=gv.inputHeight)

        # general
        elif globe.emp_access == 2:
            # Disable Button

            # Disable Entry Fields
            gv.fNameInput.config(state=DISABLED)
            gv.lNameInput.config(state=DISABLED)
            gv.classInput.config(state=DISABLED)
            gv.empNumInput.config(state=DISABLED)
            gv.passwordInput.config(state=DISABLED)
            gv.payYTDInput.config(state=DISABLED)

            # Buttons
            gv.saveProfileButton.place(x=0, y=40)

            # Define save profile button
            gv.saveProfileButton.config(command=self.save_profile)

            # Labels
            gv.fNameLabel.place(x=200, y=50)
            gv.lNameLabel.place(x=200, y=75)
            gv.phoneLabel.place(x=200, y=100)
            gv.classificationLabel.place(x=200, y=125)
            gv.empNumberLabel.place(x=200, y=150)
            gv.passwordLabel.place(x=200, y=175)
            gv.departmentLabel.place(x=200, y=200)
            gv.payRateLabel.place(x=200, y=225)
            gv.payYTDLabel.place(x=200, y=250)

            # Inputs
            gv.fNameInput.place(x=340, y=50,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.lNameInput.place(x=340, y=75,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.phoneInput.place(x=340, y=100,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.classInput.place(x=340, y=125,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.empNumInput.place(x=340, y=150,
                                 width=gv.inputWidth, height=gv.inputHeight)
            gv.passwordInput.place(x=340, y=175,
                                   width=gv.inputWidth, height=gv.inputHeight)
            gv.departmentInput.place(x=340, y=200,
                                     width=gv.inputWidth,
                                     height=gv.inputHeight)
            gv.payRateInput.place(x=340, y=225,
                                  width=gv.inputWidth, height=gv.inputHeight)
            gv.payYTDInput.place(x=340, y=250,
                                 width=gv.inputWidth, height=gv.inputHeight)

        # employee
        elif globe.emp_access == 3:
            # Disable Button

            # Disable Entry Fields
            gv.fNameInput.config(state=DISABLED)
            gv.lNameInput.config(state=DISABLED)
            gv.phoneInput.config(state=DISABLED)
            gv.departmentInput.config(state=DISABLED)

            # Buttons

            # Define save profile button

            # Labels
            gv.fNameLabel.place(x=200, y=50)
            gv.lNameLabel.place(x=200, y=75)
            gv.phoneLabel.place(x=200, y=100)
            gv.departmentLabel.place(x=200, y=125)

            # Inputs
            gv.fNameInput.place(x=340, y=50,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.lNameInput.place(x=340, y=75,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.phoneInput.place(x=340, y=100,
                                width=gv.inputWidth, height=gv.inputHeight)
            gv.departmentInput.place(x=340, y=125,
                                     width=gv.inputWidth,
                                     height=gv.inputHeight)

        else:
            messagebox.showinfo("Error", "You do not have access. If you think you should please contact your system administrator.")

    def save_profile(self):
        globe.pr.new_user(gv.emp_num_var.get(), gv.fname_var.get(), gv.lname_var.get(), gv.address_var.get(),
                          gv.address2_var.get(), gv.city_var.get(), gv.state_var.get(), gv.zip_var.get(),
                          gv.class_var.get(), gv.pay_ytd_var.get(), gv.pay_rate_var.get(), gv.passw_var.get(),
                          gv.security_var.get(), gv.phone_var.get(), gv.department_var.get())
