"""
Payroll Processing page
"""

from tkinter import *

# Create our frame
root = Tk()
root.geometry("925x500")
root.title('Payroll Processing Excellence: Team 5')

# Create the standard for buttons
buttonColor = '#ffffff'
buttonWidth = 20
buttonHeight = 2
inputWidth = 160
inputHeight = 22
inputEditColor = 'white'
inputReadColor = 'Gray'
inputBorderWidth = 1


def main():
    # Global Variables
    global employeesButton
    global timeCardsButton
    global salesButton
    global myProfileButton
    global processPayrollButton
    global importTimecardButton
    global importSalesButton
    global payrollButton

    global payrollDesc
    global timecardDesc
    global salesDesc

    # Object list
    payrollDesc = Label(root, text="Will process payroll for current pay cycle")
    timecardDesc = Label(root, text="Takes you to import timecards")
    salesDesc = Label(root, text="Takes you to import sales reports")

    spacer = Label(root, text="        ")

    # button
    employeesButton = Button(root, text="Employee's",
                             width=buttonWidth, bg=buttonColor,
                             height=buttonHeight,
                             command=employees)
    timeCardsButton = Button(root, text='Timecards', width=buttonWidth,
                             height=buttonHeight, bg=buttonColor,
                             command=timecards)
    salesButton = Button(root, text='   Sales   ', width=buttonWidth,
                         height=buttonHeight,
                         command=sales, bg=buttonColor)
    myProfileButton = Button(root, text='My Profile', width=buttonWidth,
                             height=buttonHeight,
                             command=my_profile, bg=buttonColor)
    processPayrollButton = Button(root, text='Process Payroll', width=buttonWidth,
                                  height=buttonHeight,
                                  command=process_payroll, bg=buttonColor)
    importTimecardButton = Button(root, text='Import Timecards', width=buttonWidth,
                                  height=buttonHeight,
                                  command=import_timecards, bg=buttonColor)
    importSalesButton = Button(root, text='Import Sales',
                               width=buttonWidth, height=buttonHeight,
                               command=import_sales,
                               bg=buttonColor)
    payrollButton = Button(root, text="Payroll", width=buttonWidth,
                           height=buttonHeight, command=payroll, bg=buttonColor, state=DISABLED)

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

    # Loop Tkinter
    root.mainloop()


# Declare methods for each button
def employees():
    pass


def timecards():
    pass


def sales():
    pass


def my_profile():
    pass


def new_employee():
    pass


def find_employee():
    pass


def import_employee():
    pass


def payroll():
    pass


def process_payroll():
    pass


def import_timecards():
    pass


def import_sales():
    pass


if __name__ == '__main__':
    main()
