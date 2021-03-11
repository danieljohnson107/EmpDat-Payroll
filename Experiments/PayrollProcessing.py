"""
Payroll Processing page
"""

from tkinter import *
from tkinter import *
from UserData import *
from GuiValues import *
import main as m


class PayrollProcessing(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        gv.processPayrollButton.place(x=0, y=40)
        gv.importTimecardButton.place(x=0, y=80)
        gv.importSalesButton.place(x=0, y=120)

        gv.payrollDesc.place(x=200, y=50)
        gv.timecardDesc.place(x=200, y=90)
        gv.salesDesc.place(x=200, y=130)

    # Declare methods for each button
    def employees(self):
        self.controller.show_frame("FindEmployee")

    def timecards(self):
        pass

    def sales(self):
        pass

    def my_profile(self):
        self.controller.show_frame("MyProfile")

    def process_payroll(self):
        self.controller.show_frame("PayrollProcessing")

    def import_timecards(self):
        pass

    def import_sales(self):
        pass
