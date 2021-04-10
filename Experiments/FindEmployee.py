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
        results.clear()

    def edit_pressed(self):

        openThis = gv.results_entry.get(ANCHOR)
        