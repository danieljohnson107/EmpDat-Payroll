"""
Class file to save all global gui variables
"""

from tkinter import *
import GlobalVariables as globe
from tkinter.filedialog import askopenfilename
import pandas as pd


class GuiValues(Frame):

    def __init__(self, frame, controller):
        Frame.__init__(self, frame)

        #list of options for select lists
        classifications = [
            'Hourly',
            'Salary',
            'Commission',
        ]
        securityAssess = [
            'Admin',
            'General Manager',
            'Employee',
        ]

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

        # Entry variables
        self.name_var = StringVar()
        self.passw_var = StringVar()
        self.confirm_passw_var = StringVar()
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.address_var = StringVar()
        self.address2_var = StringVar()
        self.city_var = StringVar()
        self.state_var = StringVar()
        self.zip_var = StringVar()
        self.phone_var = StringVar()
        self.class_var = StringVar()
        self.emp_num_var = StringVar()
        self.department_var = StringVar()
        self.pay_rate_var = StringVar()
        self.pay_ytd_var = StringVar()
        self.security_var = StringVar()
        self.results_var = StringVar()

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
                                      command=lambda: self.openNewWindow("Timecards"))
        self.salesButton = Button(frame, text='Sales',
                                  width=self.buttonWidth,
                                  height=self.buttonHeight,
                                  bg=self.buttonColor,
                                  fg=self.buttonTextColor,
                                  command=lambda: self.openNewWindow("Sales"))
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
                                           command=lambda: self.openNewWindow("New Employee"))
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
        self.search_button = Button(frame, text='Search',
                                    width=self.buttonWidth,
                                    height=self.buttonHeight,
                                    bg=self.buttonColor,
                                    fg=self.buttonTextColor,
                                    command=self.search_pressed)
        self.edit_button = Button(frame, text='View',
                                  width=self.buttonWidth,
                                  height=self.buttonHeight,
                                  bg=self.buttonColor,
                                  fg=self.buttonTextColor,
                                  command=self.edit_pressed)

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
        self.results_label = Label(frame, text="Results:")

        # Inputs
        self.fNameInput = Entry(frame, textvariable=self.fname_var,
                                bg=self.inputEditColor,
                                borderwidth=self.inputBorderWidth)
        self.lNameInput = Entry(frame, textvariable=self.lname_var,
                                bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.addressInput = Entry(frame, textvariable=self.address_var, bg=self.inputEditColor,
                                  borderwidth=self.inputBorderWidth)
        self.addressTwoInput = Entry(frame, textvariable=self.address2_var,
                                     bg=self.inputEditColor,
                                     borderwidth=self.inputBorderWidth)
        self.cityInput = Entry(frame, textvariable=self.city_var,
                               bg=self.inputEditColor,
                               borderwidth=self.inputBorderWidth)
        self.stateInput = Entry(frame, textvariable=self.state_var,
                                bg=self.inputEditColor, borderwidth=self.inputBorderWidth)
        self.zipInput = Entry(frame, textvariable=self.zip_var, bg=self.inputEditColor,
                              borderwidth=self.inputBorderWidth)
        self.phoneInput = Entry(frame, textvariable=self.phone_var,
                                bg=self.inputEditColor,
                                borderwidth=self.inputBorderWidth)
        self.classInput = Entry(frame, textvariable=self.class_var,
                                bg=self.inputEditColor,
                                borderwidth=self.inputBorderWidth)
        self.empNumInput = Entry(frame, textvariable=self.emp_num_var,
                                 bg=self.inputEditColor,
                                 borderwidth=self.inputBorderWidth)
        self.passwordInput = Entry(frame, textvariable=self.passw_var,
                                   bg=self.inputEditColor,
                                   borderwidth=self.inputBorderWidth)
        self.departmentInput = Entry(frame, textvariable=self.department_var,
                                     bg=self.inputEditColor,
                                     borderwidth=self.inputBorderWidth)
        self.payRateInput = Entry(frame, textvariable=self.pay_rate_var,
                                  bg=self.inputEditColor,
                                  borderwidth=self.inputBorderWidth)
        self.payYTDInput = Entry(frame, textvariable=self.pay_ytd_var,
                                 bg=self.inputEditColor,
                                 borderwidth=self.inputBorderWidth)
        self.securityInput = Entry(frame, textvariable=self.security_var,
                                   bg=self.inputEditColor,
                                   borderwidth=self.inputBorderWidth)
        self.user_entry = Entry(frame, textvariable=self.name_var,
                                font=self.fontProp)
        self.password_entry = Entry(frame, textvariable=self.passw_var,
                                    show="*",
                                    font=self.fontProp)
        self.set_password_entry = Entry(frame, textvariable=self.passw_var,
                                        show="*",
                                        font=self.fontProp)
        self.confirm_password_entry = Entry(frame, textvariable=self.confirm_passw_var,
                                            show="*",
                                            font=self.fontProp)
        self.results_entry = Listbox(frame, bg=self.inputEditColor,
                                     borderwidth=self.inputBorderWidth)

    def create_nav_bar(self):
        if globe.emp_access == 1:
            self.employeesButton.place(x=0, y=0)
            self.timeCardsButton.place(x=185, y=0)
            self.salesButton.place(x=370, y=0)
            self.payrollButton.place(x=555, y=0)
            self.myProfileButton.place(x=740, y=0)
        else:
            self.employeesButton.place(x=0, y=0)
            self.myProfileButton.place(x=185, y=0)

    def my_profile_values(self):
        emp_id = globe.pr.current_emp
        user = globe.pr.get_profile(emp_id)

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
        self.fNameInput.insert(0, user[1])
        self.lNameInput.insert(0, user[2])
        self.addressInput.insert(0, user[3])
        self.addressTwoInput.insert(0, user[4])
        self.cityInput.insert(0, user[5])
        self.stateInput.insert(0, user[6])
        self.zipInput.insert(0, user[7])
        self.phoneInput.insert(0, user[14])
        self.classInput.insert(0, user[8])
        self.empNumInput.insert(0, user[0])
        self.passwordInput.insert(0, user[12])
        self.departmentInput.insert(0, user[15])
        self.payRateInput.insert(0, user[11])
        self.payYTDInput.insert(0, user[9])
        self.securityInput.insert(0, user[13])

    def openNewWindow(self, title):
        master = Tk()

        master.geometry("800x300")

        master.title(title)

        typeLabel = Label(master, text=title+" file must be a .txt or .csv file.")
        fileInputLabel = Label(master, text="File for import:")
        inputField= Entry(master, bg=self.inputEditColor, state='disabled', width=50)
        uploadButton = Button(master, text="Upload",
                              width=self.buttonWidth,
                              bg=self.buttonColor,
                              fg=self.buttonTextColor,
                              height=self.buttonHeight,
                              command=lambda:[inputField.config(state='normal'),inputField.delete(0,END), inputField.insert(0, self.getFileName()), inputField.config(state='readonly')])
        submitButton = Button(master, text="Submit",
                              width=self.buttonWidth,
                              bg=self.buttonColor,
                              fg=self.buttonTextColor,
                              height=self.buttonHeight,
                              command=lambda:[self.uploadFile(inputField.get(), title), master.destroy()])

        typeLabel.place(x=100, y=50)
        fileInputLabel.place(x=100, y=100)
        inputField.place(x=200, y=100)
        uploadButton.place(x=100, y=150)
        submitButton.place(x=400, y=150)

    def getFileName(self):
        return askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])

    def uploadFile(self, filePath, fileType):
        try:
            uploadedFile = pd.read_csv(filePath)
            if(fileType == 'Timecards'):
                globe.timecardsFile = uploadedFile
                # print(globe.timecardsFile)
            else:
                globe.salesFile = uploadedFile
                # print(globe.salesFile)

            # print('fp', filePath)
            # print('hi', uploadedFile)
        except:
            print("There was an error submitting the file")

    def search_pressed(self):

        searchNumber = self.empNumInput.get()
        searchfName = self.fNameInput.get()
        searchlName = self.lNameInput.get()
        searchPhone = self.phoneInput.get()

        results = []
        results.clear()
        self.results_entry.delete(0, END)

        if (searchNumber != ''):
            firstName = globe.ud.read_value(searchNumber, 'first_name')
            lastName = globe.ud.read_value(searchNumber, 'last_name')
            userDepartment = globe.ud.read_value(searchNumber, 'department')

            results.append(lastName + ', ' + firstName + ' Dept:' + userDepartment + ' id:' + searchNumber)

        elif (searchfName != ''):
            firstNameResults = globe.ud.get_match(searchfName)
            for person in firstNameResults:
                firstName = globe.ud.read_value(person, 'first_name')
                lastName = globe.ud.read_value(person, 'last_name')
                userDepartment = globe.ud.read_value(person, 'department')

                results.append(lastName + ', ' + firstName + ' Dept:' + userDepartment + ' id:' + person)

        elif (searchlName != ''):
            lastNameResults = globe.ud.get_match('', searchlName)
            for person in lastNameResults:
                firstName = globe.ud.read_value(person, 'first_name')
                lastName = globe.ud.read_value(person, 'last_name')
                userDepartment = globe.ud.read_value(person, 'department')

                results.append(lastName + ', ' + firstName + ' Dept:' + userDepartment + ' id:' + person)

        elif (searchPhone != ''):
            phoneNumberResults = globe.ud.get_match('', '', searchPhone)
            for person in phoneNumberResults:
                firstName = globe.ud.read_value(person, 'first_name')
                lastName = globe.ud.read_value(person, 'last_name')
                userDepartment = globe.ud.read_value(person, 'department')

                results.append(lastName + ', ' + firstName + ' Dept:' + userDepartment + ' id:' + person)
        else:
            messagebox.showwarning('No Values Entered', 'You must enter a value in one of the search boxes to get a search result.')

        results.sort()
        if len(results) == 0:
            results.append('No results found')

        for item in results:
            self.results_entry.insert(END, item)

    def edit_pressed(self):
        self.controller.show_frame("EditEmployee")

    def edit_profile_values(self):
        openThis = self.results_entry.get(ANCHOR)
        indId = openThis.index('id:')
        indId += 3
        searchID = openThis[indId:]
        user = globe.pr.get_profile(searchID)

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
        self.fNameInput.insert(0, user[1])
        self.lNameInput.insert(0, user[2])
        self.addressInput.insert(0, user[3])
        self.addressTwoInput.insert(0, user[4])
        self.cityInput.insert(0, user[5])
        self.stateInput.insert(0, user[6])
        self.zipInput.insert(0, user[7])
        self.phoneInput.insert(0, user[14])
        self.classInput.insert(0, user[8])
        self.empNumInput.insert(0, user[0])
        self.passwordInput.insert(0, user[12])
        self.departmentInput.insert(0, user[15])
        self.payRateInput.insert(0, user[11])
        self.payYTDInput.insert(0, user[9])
        self.securityInput.insert(0, user[13])
