"""
Payroll Processing page
"""

from tkinter import messagebox, Frame, DISABLED, NORMAL
from GuiValues import GuiValues
import GlobalVariables as Globe


class PayrollProcessing(Frame):
    """Class for Payroll Processing frame"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        global gv
        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        gv.process_payroll_button.place(x=0, y=40)
        gv.import_timecard_button.place(x=0, y=80)
        gv.import_sales_button.place(x=0, y=120)

        gv.payroll_desc.place(x=200, y=50)
        gv.timecard_desc.place(x=200, y=90)
        gv.sales_desc.place(x=200, y=130)

        # Disable the process payroll if there aren't the sales and timecards files
        if Globe.sales_file is None and Globe.timecards_file is None or \
                Globe.timecards_file is None or Globe.sales_file is None:
            gv.process_payroll_button.config(state=DISABLED)
        else:
            gv.process_payroll_button.config(state=NORMAL)

        gv.process_payroll_button.config(command=self.process_payroll)
        gv.import_timecard_button.config(command=lambda: gv.open_new_window("Timecards"))
        gv.import_sales_button.config(command=lambda: gv.open_new_window("Sales"))

    @staticmethod
    def process_payroll():
        """Method for Process button press"""
        # Process Payroll
        try:
            Globe.Pr.run_payroll()
            messagebox.showinfo("Success!", "Payroll was Successfully Processed. "
                                            "Log file is now available.")
        except Exception as error:
            messagebox.showinfo("Error!", f"There was an Error in Processing Payroll! "
                                          f"Please Contact your Administrator: {error}")

        # Reset the values and refresh the page
        Globe.timecards_file = None
        Globe.sales_file = None
        gv.payroll_processing_refresh()
