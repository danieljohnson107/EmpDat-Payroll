"""
Payroll Processing page
"""

from tkinter import *
from tkinter import *
from UserData import *
from GuiValues import *
import main as m

gv = GuiValues()

# Create our frame
# self = Tk()


class PayrollProcessing(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Object list
        payrollDesc = Label(self,
                            text="Will process payroll for current pay cycle")
        timecardDesc = Label(self, text="Takes you to import timecards")
        salesDesc = Label(self, text="Takes you to import sales reports")

        spacer = Label(self, text="        ")

        # button
        employeesButton = Button(self, text="Employee's",
                                 width=gv.buttonWidth, bg=gv.buttonColor,
                                 height=gv.buttonHeight,
                                 command=self.employees)
        timeCardsButton = Button(self, text='Timecards', width=gv.buttonWidth,
                                 height=gv.buttonHeight, bg=gv.buttonColor,
                                 command=self.timecards)
        salesButton = Button(self, text='   Sales   ', width=gv.buttonWidth,
                             height=gv.buttonHeight,
                             command=self.sales, bg=gv.buttonColor)
        myProfileButton = Button(self, text='My Profile', width=gv.buttonWidth,
                                 height=gv.buttonHeight,
                                 command=self.my_profile, bg=gv.buttonColor)
        processPayrollButton = Button(self, text='Process Payroll',
                                      width=gv.buttonWidth,
                                      height=gv.buttonHeight,
                                      command=self.process_payroll,
                                      bg=gv.buttonColor)
        importTimecardButton = Button(self, text='Import Timecards',
                                      width=gv.buttonWidth,
                                      height=gv.buttonHeight,
                                      command=self.import_timecards,
                                      bg=gv.buttonColor)
        importSalesButton = Button(self, text='Import Sales',
                                   width=gv.buttonWidth,
                                   height=gv.buttonHeight,
                                   command=self.import_sales,
                                   bg=gv.buttonColor)
        payrollButton = Button(self, text="Payroll", width=gv.buttonWidth,
                               height=gv.buttonHeight,
                               bg=gv.buttonColor, state=DISABLED)

        # location of items on the screen
        # set all locations on form
        # buttons
        employeesButton.place(x=0, y=0)
        timeCardsButton.place(x=185, y=0)
        salesButton.place(x=370, y=0)
        payrollButton.place(x=555, y=0)
        myProfileButton.place(x=740, y=0)
        processPayrollButton.place(x=0, y=70)
        importTimecardButton.place(x=0, y=140)
        importSalesButton.place(x=0, y=210)

        # Labels
        payrollDesc.place(x=200, y=85)
        timecardDesc.place(x=200, y=152)
        salesDesc.place(x=200, y=220)

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
