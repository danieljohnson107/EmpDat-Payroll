from GuiValues import *
import GlobalVariables as globe
from tkinter import messagebox

''' to use images yoy need to install pillow
install with "pip install pillow" on your python to use
ImageTk.PhotoImage(Image.open("imagename.png"))
put image in widget
then put on page
'''

''' everything is a widget
start with a self
 widget
this shoudl be first every time you use tkinter'''
'''define the action the function will take'''


class MyProfile(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        controller = controller

        # Initialize gui components and make global
        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        # Disable Button
        gv.myProfileButton.config(state=DISABLED)

        # Buttons
        gv.employeesButton.place(x=0, y=0)
        gv.timeCardsButton.place(x=185, y=0)
        gv.salesButton.place(x=370, y=0)
        gv.payrollButton.place(x=555, y=0)
        gv.myProfileButton.place(x=740, y=0)
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
        gv.fNameInput.place(x=340, y=50, width=gv.inputWidth, height=gv.inputHeight)
        gv.lNameInput.place(x=340, y=75, width=gv.inputWidth, height=gv.inputHeight)
        gv.addressInput.place(x=340, y=100, width=gv.inputWidth, height=gv.inputHeight)
        gv.addressTwoInput.place(x=340, y=125, width=gv.inputWidth, height=gv.inputHeight)
        gv.cityInput.place(x=340, y=150, width=gv.inputWidth, height=gv.inputHeight)
        gv.stateInput.place(x=340, y=175, width=gv.inputWidth, height=gv.inputHeight)
        gv.zipInput.place(x=340, y=200, width=gv.inputWidth, height=gv.inputHeight)
        gv.phoneInput.place(x=340, y=225, width=gv.inputWidth, height=gv.inputHeight)
        gv.classInput.place(x=340, y=250, width=gv.inputWidth, height=gv.inputHeight)
        gv.empNumInput.place(x=340, y=275, width=gv.inputWidth, height=gv.inputHeight)
        gv.passwordInput.place(x=340, y=300, width=gv.inputWidth, height=gv.inputHeight)
        gv.departmentInput.place(x=340, y=325, width=gv.inputWidth, height=gv.inputHeight)
        gv.payRateInput.place(x=340, y=350, width=gv.inputWidth, height=gv.inputHeight)
        gv.payYTDInput.place(x=340, y=375, width=gv.inputWidth, height=gv.inputHeight)
        gv.securityInput.place(x=340, y=400, width=gv.inputWidth, height=gv.inputHeight)

        # fill the fields
        gv.my_profile_values()

    def save_profile(self):

        # Grab the new info
        fname = gv.fname_var.get()
        lname = gv.lname_var.get()
        address = gv.address_var.get()
        address2 = gv.address2_var.get()
        city = gv.city_var.get()
        state = gv.state_var.get()
        zip = gv.zip_var.get()
        phone = gv.phone_var.get()
        classification = gv.class_var.get()
        emp_num = gv.emp_num_var.get()
        password = gv.passw_var.get()
        department = gv.department_var.get()
        pay_rate = gv.pay_rate_var.get()
        pay_ytd = gv.pay_ytd_var.get()
        security = gv.security_var.get()

        # Set the new values
        globe.ud.change_field(globe.ud.employee_number, fname, 'first_name')
        globe.ud.change_field(globe.ud.employee_number, lname, 'last_name')
        globe.ud.change_field(globe.ud.employee_number, address, 'address')
        globe.ud.change_field(globe.ud.employee_number, address2, 'address2')
        globe.ud.change_field(globe.ud.employee_number, city, 'city')
        globe.ud.change_field(globe.ud.employee_number, state, 'state')
        globe.ud.change_field(globe.ud.employee_number, zip, 'zip')
        globe.ud.change_field(globe.ud.employee_number, phone, 'phone_number')
        globe.ud.change_field(globe.ud.employee_number, classification, 'classification')
        globe.ud.change_field(globe.ud.employee_number, password, 'password')
        globe.ud.change_field(globe.ud.employee_number, department, 'department')
        globe.ud.change_field(globe.ud.employee_number, pay_rate, 'hourly')
        globe.ud.change_field(globe.ud.employee_number, pay_ytd, 'salary')
        globe.ud.change_field(globe.ud.employee_number, security, 'access')
        globe.ud.change_field(globe.ud.employee_number, emp_num, 'id')

        # Pop up letting them know that it updated successfully
        messagebox.showinfo("Success!", "Successfully Updated")
