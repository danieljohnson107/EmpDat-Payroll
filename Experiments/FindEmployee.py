"""Class file for Find Employee frame"""

from tkinter import messagebox, Frame, DISABLED
from GuiValues import GuiValues
import GlobalVariables as Globe


class FindEmployee(Frame):
    """Class for the find employee frame"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        if Globe.EMPACCESS == 1:
            # Disable button
            gv.find_employee_button.config(state=DISABLED)
            gv.employees_button.config(state=DISABLED)
            gv.results_entry.bind("<<ListboxSelect>>", gv.set_anchor)

            # Create buttons
            gv.new_employee_button.place(x=0, y=40)
            gv.find_employee_button.place(x=0, y=80)
            gv.import_employee_button.place(x=0, y=120)
            gv.search_button.place(x=600, y=50)
            gv.edit_button.place(x=600, y=200)

            # Labels
            gv.emp_number_label.place(x=200, y=50)
            gv.f_name_label.place(x=200, y=75)
            gv.l_name_label.place(x=200, y=100)
            gv.phone_label.place(x=200, y=125)
            gv.results_label.place(x=200, y=200)

            # Inputs
            gv.emp_num_input.place(x=340, y=50, width=240, height=gv.input_height)
            gv.f_name_input.place(x=340, y=75, width=240, height=gv.input_height)
            gv.l_name_input.place(x=340, y=100, width=240, height=gv.input_height)
            gv.phone_input.place(x=340, y=125, width=240, height=gv.input_height)
            gv.results_entry.place(x=340, y=200, width=240, height=100)
        elif Globe.EMPACCESS == 2:
            # Disable button
            gv.find_employee_button.config(state=DISABLED)
            gv.results_entry.bind("<<ListboxSelect>>", gv.set_anchor)

            # Create buttons
            gv.find_employee_button.place(x=0, y=40)
            gv.search_button.place(x=600, y=50)
            gv.edit_button.place(x=600, y=200)

            # Labels
            gv.f_name_label.place(x=200, y=50)
            gv.l_name_label.place(x=200, y=75)
            gv.phone_label.place(x=200, y=100)
            gv.results_label.place(x=200, y=200)

            # Inputs
            gv.f_name_input.place(x=340, y=50, width=240, height=gv.input_height)
            gv.l_name_input.place(x=340, y=75, width=240, height=gv.input_height)
            gv.phone_input.place(x=340, y=100, width=240, height=gv.input_height)
            gv.results_entry.place(x=340, y=200, width=240, height=100)
        elif Globe.EMPACCESS == 3:
            # Disable button
            gv.find_employee_button.config(state=DISABLED)
            gv.results_entry.bind("<<ListboxSelect>>", gv.set_anchor)

            # Create buttons
            gv.find_employee_button.place(x=0, y=80)
            gv.search_button.place(x=600, y=50)
            gv.edit_button.place(x=600, y=200)

            # Labels
            gv.f_name_label.place(x=200, y=50)
            gv.l_name_label.place(x=200, y=75)
            gv.phone_label.place(x=200, y=100)
            gv.results_label.place(x=200, y=200)

            # Inputs
            gv.f_name_input.place(x=340, y=50, width=240, height=gv.input_height)
            gv.l_name_input.place(x=340, y=75, width=240, height=gv.input_height)
            gv.phone_input.place(x=340, y=100, width=240, height=gv.input_height)
            gv.results_entry.place(x=340, y=200, width=240, height=100)

        else:
            messagebox.showwarning("Error", "You are not authorized to be here. You were never here...;)")

        self.controller.bind('<Return>', lambda event: gv.search_pressed())
