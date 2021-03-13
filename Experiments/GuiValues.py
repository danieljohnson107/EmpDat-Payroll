"""
Class file to save all global gui variables
"""

from tkinter import *
import GlobalVariables as globe


class GuiValues(Frame):

    def __init__(self, frame, controller):
        Frame.__init__(self, frame)

        self.parent = frame
        self.controller = controller
        self.count = 0

        # Create the standard for buttons
        self.buttonColor = '#2c71de'
        self.buttonWidth = 20
        self.buttonHeight = 2
        self.inputWidth = 380
        self.inputHeight = 22
        self.inputEditColor = 'white'
        self.inputReadColor = 'Gray'
        self.inputBorderWidth = 1
        self.buttonTextColor = "white"
        self.fontProp = ('calibre', 14, 'normal')

        # Login page variables
        self.name_var = StringVar()
        self.passw_var = StringVar()
        self.confirm_passw_var = StringVar()

        # Buttons
        self.employeesButton = Button(frame, text='Employees',
                                      width=self.buttonWidth,
                                      height=self.buttonHeight,
                                      bg=self.buttonColor,
                                      fg=self.buttonTextColor,
                                      command=lambda: self.controller.show_frame("FindEmployee"))
        self.timeCardsButton = Button(frame, text='Timecards',
                                      width=self.buttonWidth,
                                      height=self.buttonHeight,
                                      bg=self.buttonColor,
                                      fg=self.buttonTextColor,
                                      command=lambda: self.controller.show_frame("FindEmployee"))
        self.salesButton = Button(frame, text='Sales',
                                  width=self.buttonWidth,
                                  height=self.buttonHeight,
                                  bg=self.buttonColor,
                                  fg=self.buttonTextColor,
                                  command=lambda: self.controller.show_frame("FindEmployee"))
        self.myProfileButton = Button(frame, text='My Profile',
                                      width=self.buttonWidth,
                                      height=self.buttonHeight,
                                      bg=self.buttonColor,
                                      fg=self.buttonTextColor,
                                      command=lambda: self.controller.show_frame("MyProfile"))
        self.newEmployeeButton = Button(frame, text='Enter New\nEmployee',
                                        width=self.buttonWidth,
                                        height=self.buttonHeight,
                                        bg=self.buttonColor,
                                        fg=self.buttonTextColor,
                                        command=lambda: self.controller.show_frame("EnterNewEmployee"))
        self.findEmployeeButton = Button(frame, text='Find Employee',
                                         width=self.buttonWidth,
                                         height=self.buttonHeight,
                                         bg=self.buttonColor,
                                         fg=self.buttonTextColor,
                                         command=lambda: self.controller.show_frame("FindEmployee"))
        self.importEmployeeButton = Button(frame, text='Import txt of\nnew Employees',
                                           width=self.buttonWidth,
                                           height=self.buttonHeight,
                                           bg=self.buttonColor,
                                           fg=self.buttonTextColor,
                                           command=lambda: self.controller.show_frame("FindEmployee"))
        self.saveProfileButton = Button(frame, text='Save',
                                        width=self.buttonWidth,
                                        height=self.buttonHeight,
                                        bg=self.buttonColor,
                                        fg=self.buttonTextColor,
                                        command=lambda: self.controller.show_frame("FindEmployee"))
        self.payrollButton = Button(frame, text="Payroll",
                                    width=self.buttonWidth,
                                    height=self.buttonHeight,
                                    bg=self.buttonColor,
                                    fg=self.buttonTextColor,
                                    command=lambda: self.controller.show_frame("PayrollProcessing"))
        self.login_button = Button(frame, text="Login",
                                   width=self.buttonWidth,
                                   height=self.buttonHeight,
                                   bg=self.buttonColor,
                                   fg=self.buttonTextColor,
                                   font=self.fontProp)
        self.create_password_button = Button(frame, text="Don't Have a Password?",
                                             width=self.buttonWidth,
                                             height=self.buttonHeight,
                                             bg=self.buttonColor,
                                             fg=self.buttonTextColor,
                                             font=self.fontProp,
                                             command=lambda: self.controller.show_frame("ChangePassword"))
        self.processPayrollButton = Button(frame, text='Process Payroll',
                                           width=self.buttonWidth,
                                           height=self.buttonHeight,
                                           bg=self.buttonColor,
                                           fg=self.buttonTextColor)
        self.importTimecardButton = Button(frame, text='Import Timecards',
                                           width=self.buttonWidth,
                                           height=self.buttonHeight,
                                           bg=self.buttonColor,
                                           fg=self.buttonTextColor)
        self.importSalesButton = Button(frame, text='Import Sales',
                                        width=self.buttonWidth,
                                        height=self.buttonHeight,
                                        bg=self.buttonColor,
                                        fg=self.buttonTextColor)
        self.set_password_button = Button(frame, text="Set Password",
                                          width=self.buttonWidth,
                                          height=self.buttonHeight,
                                          bg=self.buttonColor,
                                          fg=self.buttonTextColor,
                                          font=self.fontProp)
        self.cancel_button = Button(frame, text="Cancel",
                                    width=self.buttonWidth,
                                    height=self.buttonHeight,
                                    bg=self.buttonColor,
                                    fg=self.buttonTextColor,
                                    font=self.fontProp,
                                    command=lambda: self.controller.show_frame("LoginPage"))

        # Labels
        self.fNameLabel = Label(frame, text="First Name:")
        self.lNameLabel = Label(frame, text="Last Name:")
        self.addressLabel = Label(frame, text='Address:')
        self.addressLineTwoLabel = Label(frame, text='Address Line 2:')
        self.cityLabel = Label(frame, text='City:')
        self.stateLabel = Label(frame, text='State:')
        self.zipCodeLabel = Label(frame, text='Zip:')
        self.phoneLabel = Label(frame, text='Phone Number:')
        self.classificationLabel = Label(frame, text='Classification:')
        self.empNumberLabel = Label(frame, text='Employee Number:')
        self.passwordLabel = Label(frame, text='Password:')
        self.departmentLabel = Label(frame, text='Department:')
        self.payRateLabel = Label(frame, text='Pay Rate:')
        self.payYTDLabel = Label(frame, text='Pay YTD:')
        self.securityAccessLabel = Label(frame, text='Security Access:')
        self.spacer = Label(frame, text="        ")
        self.employee_number_label = Label(frame, text="Employee Number", font=self.fontProp)
        self.password_label = Label(frame, text="Password", font=self.fontProp)
        self.payrollDesc = Label(frame, text="Will process payroll for current pay cycle")
        self.timecardDesc = Label(frame, text="Takes you to import timecards")
        self.salesDesc = Label(frame, text="Takes you to import sales reports")
        self.new_password_label = Label(frame, text="New Password", font=self.fontProp)
        self.confirm_password_label = Label(frame, text="Confirm Password", font=self.fontProp)

        # Inputs
        self.fNameInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.lNameInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.addressInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.addressTwoInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.cityInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.stateInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.zipInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.phoneInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.classInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.empNumInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.passwordInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.departmentInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.payRateInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.payYTDInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.securityInput = Entry(frame, bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.user_entry = Entry(frame, textvariable=self.name_var, font=self.fontProp)
        self.password_entry = Entry(frame, textvariable=self.passw_var, show="*", font=self.fontProp)
        self.set_password_entry = Entry(frame, textvariable=self.passw_var, show="*", font=self.fontProp)
        self.confirm_password_entry = Entry(frame, textvariable=self.confirm_passw_var, show="*", font=self.fontProp)

    def create_nav_bar(self):
        self.employeesButton.place(x=0, y=0)
        self.timeCardsButton.place(x=185, y=0)
        self.salesButton.place(x=370, y=0)
        self.payrollButton.place(x=555, y=0)
        self.myProfileButton.place(x=740, y=0)

    def my_profile_values(self):
        self.controller.show_frame("MyProfile")

        emp_id = globe.ud.employee_number

        # Clear all fields in case of double click
        self.fNameInput.delete(0, "end")
        self.fNameInput.delete(0, "end")
        self.lNameInput.delete(0, "end")
        self.addressInput.delete(0, "end")
        self.addressTwoInput.delete(0, "end")
        self.cityInput.delete(0, "end")
        self.stateInput.delete(0, "end")
        self.zipInput.delete(0, "end")
        self.phoneInput.delete(0, "end")
        self.classInput.delete(0, "end")
        self.empNumInput.delete(0, "end")
        self.passwordInput.delete(0, "end")
        self.departmentInput.delete(0, "end")
        self.payRateInput.delete(0, "end")
        self.payYTDInput.delete(0, "end")
        self.securityInput.delete(0, "end")

        # Insert values from CSV
        self.fNameInput.insert(0, globe.ud.read_value(emp_id, "first_name"))
        self.lNameInput.insert(0, globe.ud.read_value(emp_id, "last_name"))
        self.addressInput.insert(0, globe.ud.read_value(emp_id, "address"))
        # self.addressTwoInput.insert(0, ud.read_value(emp_id, ""))
        self.cityInput.insert(0, globe.ud.read_value(emp_id, "city"))
        self.stateInput.insert(0, globe.ud.read_value(emp_id, "state"))
        self.zipInput.insert(0, globe.ud.read_value(emp_id, "zip"))
        # self.phoneInput.insert(0, ud.read_value(emp_id, ""))
        self.classInput.insert(0, globe.ud.read_value(emp_id, "classification"))
        self.empNumInput.insert(0, globe.ud.read_value(emp_id, "id"))
        self.passwordInput.insert(0, globe.ud.read_value(emp_id, "password"))
        # self.departmentInput.insert(0, ud.read_value(emp_id, ""))
        self.payRateInput.insert(0, globe.ud.read_value(emp_id, "hourly"))
        self.payYTDInput.insert(0, globe.ud.read_value(emp_id, "salary"))
        self.securityInput.insert(0, globe.ud.read_value(emp_id, "access"))
