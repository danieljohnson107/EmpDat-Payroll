from tkinter import *

# from PIL import imageTk, Image
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
        self.controller = controller

        self.gv = GuiValues(self, controller)
        self.gv.create_nav_bar()

        # Buttons
        self.gv.employeesButton.place(x=0, y=0)
        self.gv.timeCardsButton.place(x=185, y=0)
        self.gv.salesButton.place(x=370, y=0)
        self.gv.payrollButton.place(x=555, y=0)
        self.gv.myProfileButton.place(x=740, y=0)
        self.gv.saveProfileButton.place(x=0, y=40)

        # Define save profile button
        self.gv.saveProfileButton.config(command=self.save_profile)

        # Labels
        self.gv.fNameLabel.place(x=200, y=50)
        self.gv.lNameLabel.place(x=200, y=75)
        self.gv.addressLabel.place(x=200, y=100)
        self.gv.addressLineTwoLabel.place(x=200, y=125)
        self.gv.cityLabel.place(x=200, y=150)
        self.gv.stateLabel.place(x=200, y=175)
        self.gv.zipCodeLabel.place(x=200, y=200)
        self.gv.phoneLabel.place(x=200, y=225)
        self.gv.classificationLabel.place(x=200, y=250)
        self.gv.empNumberLabel.place(x=200, y=275)
        self.gv.passwordLabel.place(x=200, y=300)
        self.gv.departmentLabel.place(x=200, y=325)
        self.gv.payRateLabel.place(x=200, y=350)
        self.gv.payYTDLabel.place(x=200, y=375)
        self.gv.securityAccessLabel.place(x=200, y=400)

        # Inputs
        self.gv.fNameInput.place(x=340, y=50, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.lNameInput.place(x=340, y=75, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.addressInput.place(x=340, y=100, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.addressTwoInput.place(x=340, y=125, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.cityInput.place(x=340, y=150, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.stateInput.place(x=340, y=175, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.zipInput.place(x=340, y=200, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.phoneInput.place(x=340, y=225, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.classInput.place(x=340, y=250, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.empNumInput.place(x=340, y=275, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.passwordInput.place(x=340, y=300, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.departmentInput.place(x=340, y=325, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.payRateInput.place(x=340, y=350, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.payYTDInput.place(x=340, y=375, width=self.gv.inputWidth, height=self.gv.inputHeight)
        self.gv.securityInput.place(x=340, y=400, width=self.gv.inputWidth, height=self.gv.inputHeight)

        # fill the fields
        self.gv.my_profile_values()

    def save_profile(self):

        # Grab the new info
        fname = self.gv.fname_var.get()
        lname = self.gv.lname_var.get()
        address = self.gv.address_var.get()
        address2 = self.gv.address2_var.get()
        city = self.gv.city_var.get()
        state = self.gv.state_var.get()
        zip = self.gv.zip_var.get()
        phone = self.gv.phone_var.get()
        classification = self.gv.class_var.get()
        emp_num = self.gv.emp_num_var.get()
        password = self.gv.passw_var.get()
        department = self.gv.department_var.get()
        pay_rate = self.gv.pay_rate_var.get()
        pay_ytd = self.gv.pay_ytd_var.get()
        security = self.gv.security_var.get()

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
