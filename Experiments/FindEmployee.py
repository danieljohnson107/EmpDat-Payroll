from GuiValues import *


class FindEmployee(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Initialize our gui components
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

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
        gv.lNameLabel.place(x=200, y=75)
        gv.phoneLabel.place(x=200, y=100)
        gv.results_label.place(x=200, y=200)

        # Inputs
        gv.empNumInput.place(x=340, y=50, width=240, height=gv.inputHeight)
        gv.lNameInput.place(x=340, y=75, width=240, height=gv.inputHeight)
        gv.phoneInput.place(x=340, y=100, width=240, height=gv.inputHeight)
        gv.results_entry.place(x=340, y=200, width=240, height=100)
