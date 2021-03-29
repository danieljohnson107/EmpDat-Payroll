"""
Payroll Processing page
"""

from tkinter import messagebox
from GuiValues import *
import GlobalVariables as g


class PayrollProcessing(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        gv = GuiValues(self, controller)
        gv.create_nav_bar()


        gv.payrollButton.config(state=DISABLED)

        gv.processPayrollButton.place(x=0, y=40)
        gv.importTimecardButton.place(x=0, y=80)
        gv.importSalesButton.place(x=0, y=120)

        gv.payrollDesc.place(x=200, y=50)
        gv.timecardDesc.place(x=200, y=90)
        gv.salesDesc.place(x=200, y=130)

        gv.importTimecardButton.config(command=lambda: gv.openNewWindow("Timecards"))
        gv.importSalesButton.config(command=lambda: gv.openNewWindow("Sales"))
        gv.processPayrollButton.config(command=self.process_payroll)

    def process_payroll(self):
        # Process Payroll
        try:
            g.pr.authenticate("57", "123")
            g.pr.run_payroll()
            messagebox.showinfo("Success!", "Payroll was Successfully Processed. Log file is now available.")
        except:
            messagebox.showinfo("Error!", "There was an Error in Processing Payroll! Please Contact your Administrator")
