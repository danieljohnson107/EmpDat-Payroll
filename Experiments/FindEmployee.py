from GuiValues import *
import app
import GlobalVariables as globe


class FindEmployee(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        if globe.emp_access == 1:
            # Disable button
            gv.findEmployeeButton.config(state=DISABLED)
            gv.employeesButton.config(state=DISABLED)

            # Create buttons
            gv.newEmployeeButton.place(x=0, y=40)
            gv.findEmployeeButton.place(x=0, y=80)
            gv.importEmployeeButton.place(x=0, y=120)
            gv.search_button.place(x=600, y=50)
            gv.edit_button.place(x=600, y=200)

            # Labels
            gv.empNumberLabel.place(x=200, y=50)
            gv.fNameLabel.place(x=200, y=75)
            gv.lNameLabel.place(x=200, y=100)
            gv.phoneLabel.place(x=200, y=125)
            gv.results_label.place(x=200, y=200)

            # Inputs
            gv.empNumInput.place(x=340, y=50, width=240, height=gv.inputHeight)
            gv.fNameInput.place(x=340, y=75, width=240, height=gv.inputHeight)
            gv.lNameInput.place(x=340, y=100, width=240, height=gv.inputHeight)
            gv.phoneInput.place(x=340, y=125, width=240, height=gv.inputHeight)
            gv.results_entry.place(x=340, y=200, width=240, height=100)
        elif globe.emp_access == 2:
            # Disable button
            gv.findEmployeeButton.config(state=DISABLED)

            # Create buttons
            gv.findEmployeeButton.place(x=0, y=40)
            gv.search_button.place(x=600, y=50)

            # Labels
            gv.fNameLabel.place(x=200, y=50)
            gv.lNameLabel.place(x=200, y=75)
            gv.phoneLabel.place(x=200, y=100)
            gv.results_label.place(x=200, y=200)

            # Inputs
            gv.fNameInput.place(x=340, y=50, width=240, height=gv.inputHeight)
            gv.lNameInput.place(x=340, y=75, width=240, height=gv.inputHeight)
            gv.phoneInput.place(x=340, y=100, width=240, height=gv.inputHeight)
            gv.results_entry.place(x=340, y=200, width=240, height=100)
        elif globe.emp_access == 3:
            # Disable button
            gv.findEmployeeButton.config(state=DISABLED)

            # Create buttons
            gv.findEmployeeButton.place(x=0, y=80)
            gv.search_button.place(x=600, y=50)

            # Labels
            gv.fNameLabel.place(x=200, y=50)
            gv.lNameLabel.place(x=200, y=75)
            gv.phoneLabel.place(x=200, y=100)
            gv.results_label.place(x=200, y=200)

            # Inputs
            gv.fNameInput.place(x=340, y=50, width=240, height=gv.inputHeight)
            gv.lNameInput.place(x=340, y=75, width=240, height=gv.inputHeight)
            gv.phoneInput.place(x=340, y=100, width=240, height=gv.inputHeight)
            gv.results_entry.place(x=340, y=200, width=240, height=100)

        else:
            messagebox.showwarning("Error", "You are not authorized to be here. You were never here...;)")

    def search_pressed(self):

        searchNumber = gv.empNumInput.get()
        searchfName = gv.fNameInput.get()
        searchlName = gv.lNameInput.get()
        searchPhone = gv.phoneInput.get()

        results = []
        results.clear()
        gv.results_entry.delete(0, END)

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
            gv.results_entry.insert(END, item)

    def edit_pressed(self):
        if gv.results_entry.get(ANCHOR):
            openThis = gv.results_entry.get(ANCHOR)
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
            
        else:
            messagebox.showwarning('You must select a person from the results to view a profile.')