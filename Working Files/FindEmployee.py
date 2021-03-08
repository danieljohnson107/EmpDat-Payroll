from tkinter import *

# from PIL import imageTk, Image
from UserData import *
from GuiValues import *
import main as m

gv = GuiValues()
''' to use images yoy need to install pillow
install with "pip install pillow" on your python to use
ImageTk.PhotoImage(Image.open("imagename.png"))
put image in widget
then put on page
'''

''' everything is a widget
start with a self
 widget
this shoudl be first every time you use tkinter'''
'''define the action the function will take'''


class FindEmployee(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Object list

        ''' to create anyting you need to do two things
        first create the item then put it in a location'''

        fNameLabel = Label(self, text="First Name:")
        lNameLabel = Label(self, text="Last Name:")
        addressLabel = Label(self, text='Address:')
        addressLineTwoLabel = Label(self, text='Address Line 2:')
        cityLabel = Label(self, text='City:')
        stateLabel = Label(self, text='State:')
        zipCodeLabel = Label(self, text='Zip:')
        phoneLabel = Label(self, text='Phone Number:')
        classificationLabel = Label(self, text='Classification:')
        empNumberLabel = Label(self, text='Employee Number:')
        passwordLabel = Label(self, text='Password:')
        departmentLabel = Label(self, text='Department:')
        payRateLabel = Label(self, text='Pay Rate:')
        payYTDLabel = Label(self, text='Pay YTD:')
        securityAccessLabel = Label(self, text='Security Access:')

        spacer = Label(self, text="        ")

        # button
        employeesButton = gv.create_button(self, "disabled", None, "Employee's")
        timeCardsButton = gv.create_button(self, "normal", None, "Timecards")
        salesButton = gv.create_button(self, "normal", None, "Sales")
        myProfileButton = gv.create_button(self, "normal", None, "My Profile")
        newEmployeeButton = gv.create_button(self, "normal", None, "Enter New\nEmployee")
        findEmployeeButton = gv.create_button(self, "normal", None, "Find Employee")
        importEmployeeButton = gv.create_button(self, "normal", None, "Import txt of\nnew Employees")
        saveProfileButton = gv.create_button(self, "normal", None, "Save")
        payrollButton = gv.create_button(self, "normal", None, "Payroll")

        # input box for client data input
        # e.get() will retreive the input from the field
        fNameInput = Entry(self, bg=gv.inputEditColor,
                           borderwidth=gv.inputBorderWidth)
        lNameInput = Entry(self, bg=gv.inputEditColor,
                           borderwidth=gv.inputBorderWidth)
        addressInput = Entry(self, bg=gv.inputEditColor,
                             borderwidth=gv.inputBorderWidth)
        addressTwoInput = Entry(self, bg=gv.inputEditColor,
                                borderwidth=gv.inputBorderWidth)
        cityInput = Entry(self, bg=gv.inputEditColor,
                          borderwidth=gv.inputBorderWidth)
        stateInput = Entry(self, bg=gv.inputEditColor,
                           borderwidth=gv.inputBorderWidth)
        zipInput = Entry(self, bg=gv.inputEditColor,
                         borderwidth=gv.inputBorderWidth)
        phoneInput = Entry(self, bg=gv.inputEditColor,
                           borderwidth=gv.inputBorderWidth)
        classInput = Entry(self, bg=gv.inputEditColor,
                           borderwidth=gv.inputBorderWidth)
        empNumInput = Entry(self, bg=gv.inputEditColor,
                            borderwidth=gv.inputBorderWidth)
        passwordInput = Entry(self, bg=gv.inputEditColor,
                              borderwidth=gv.inputBorderWidth)
        departmentInput = Entry(self, bg=gv.inputEditColor,
                                borderwidth=gv.inputBorderWidth)
        payRateInput = Entry(self, bg=gv.inputEditColor,
                             borderwidth=gv.inputBorderWidth)
        payYTDInput = Entry(self, bg=gv.inputEditColor,
                            borderwidth=gv.inputBorderWidth)
        securityInput = Entry(self, bg=gv.inputEditColor,
                              borderwidth=gv.inputBorderWidth)

        # location of items on the screen
        ''' you can put things into specific locations,
        but for now we will pack it in.

        we will usually use a place system to define locations of
        items on the interface.

        everything is a place with ys up and down and
        xs left to right.

        consider this like a table with 0 - N on the locations

        You can add these commands to the creation above as well
        if you would like. ie spacer = Label(self
        , text='').place(x=0,y=0)

        '''
        # set all locations on form
        # buttons
        employeesButton.place(x=0, y=0)
        timeCardsButton.place(x=185, y=0)
        salesButton.place(x=370, y=0)
        payrollButton.place(x=555, y=0)
        myProfileButton.place(x=740, y=0)
        newEmployeeButton.place(x=0, y=40)
        findEmployeeButton.place(x=0, y=80)
        importEmployeeButton.place(x=0, y=120)
        saveProfileButton.place(x=0, y=160)

        # Labels
        fNameLabel.place(x=200, y=40)
        lNameLabel.place(x=200, y=65)
        addressLabel.place(x=200, y=90)
        addressLineTwoLabel.place(x=200, y=115)
        cityLabel.place(x=200, y=140)
        stateLabel.place(x=200, y=165)
        zipCodeLabel.place(x=200, y=190)
        phoneLabel.place(x=200, y=215)
        classificationLabel.place(x=200, y=240)
        empNumberLabel.place(x=200, y=265)
        passwordLabel.place(x=200, y=290)
        departmentLabel.place(x=200, y=315)
        payRateLabel.place(x=200, y=340)
        payYTDLabel.place(x=200, y=365)
        securityAccessLabel.place(x=200, y=390)

        # Inputs
        fNameInput.place(x=340, y=40, width=gv.inputWidth,
                         height=gv.inputHeight)
        lNameInput.place(x=340, y=65, width=gv.inputWidth,
                         height=gv.inputHeight)
        addressInput.place(x=340, y=90, width=gv.inputWidth,
                           height=gv.inputHeight)
        addressTwoInput.place(x=340, y=115, width=gv.inputWidth,
                              height=gv.inputHeight)
        cityInput.place(x=340, y=140, width=gv.inputWidth,
                        height=gv.inputHeight)
        stateInput.place(x=340, y=165, width=gv.inputWidth,
                         height=gv.inputHeight)
        zipInput.place(x=340, y=190, width=gv.inputWidth,
                       height=gv.inputHeight)
        phoneInput.place(x=340, y=215, width=gv.inputWidth,
                         height=gv.inputHeight)
        classInput.place(x=340, y=240, width=gv.inputWidth,
                         height=gv.inputHeight)
        empNumInput.place(x=340, y=265, width=gv.inputWidth,
                          height=gv.inputHeight)
        passwordInput.place(x=340, y=290, width=gv.inputWidth,
                            height=gv.inputHeight)
        departmentInput.place(x=340, y=315, width=gv.inputWidth,
                              height=gv.inputHeight)
        payRateInput.place(x=340, y=340, width=gv.inputWidth,
                           height=gv.inputHeight)
        payYTDInput.place(x=340, y=365, width=gv.inputWidth,
                          height=gv.inputHeight)
        securityInput.place(x=340, y=390, width=gv.inputWidth,
                            height=gv.inputHeight)

    def pay(self):
        self.controller.show_frame("PayrollProcessing")

    def employees(self):
        self.controller.show_frame("FindEmployee")

    def timecards(self):
        pass

    def sales(self):
        pass

    def myProfile(self):
        self.controller.show_frame("MyProfile")

    def newEmployee(self):
        self.controller.show_frame("EnterNewEmployee")

    def findEmployee(self):
        self.controller.show_frame("FindEmployee")

    def importEmployee(self):
        pass

    def saveChanges(self):
        pass

    ''' last thing is create an event loop to watch

    the interface track location of mouse '''

    '''get buttons to do something
    create function'''
