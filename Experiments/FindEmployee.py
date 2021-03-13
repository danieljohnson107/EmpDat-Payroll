from tkinter import *

# from PIL import imageTk, Image
from GuiValues import *

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

        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        gv.newEmployeeButton.place(x=0, y=40)
        gv.findEmployeeButton.place(x=0, y=80)
        gv.importEmployeeButton.place(x=0, y=120)
        gv.saveProfileButton.place(x=0, y=160)

        # Labels
        gv.fNameLabel.place(x=200, y=50)
        gv.lNameLabel.place(x=200, y=75)
        gv.addressLabel.place(x=200, y=100)
        gv.addressLineTwoLabel.place(x=200, y=125)
        gv.cityLabel.place(x=200, y=150)
        gv.stateLabel.place(x=200, y=175)
        gv.zipCodeLabel.place(x=200, y=200)
        gv.phoneLabel.place(x=200, y=225)
        gv.classificationLabel.place(x=200, y=250)
        gv.empNumberLabel.place(x=200, y=275)
        gv.passwordLabel.place(x=200, y=300)
        gv.departmentLabel.place(x=200, y=325)
        gv.payRateLabel.place(x=200, y=350)
        gv.payYTDLabel.place(x=200, y=375)
        gv.securityAccessLabel.place(x=200, y=400)

        # Inputs
        gv.fNameInput.place(x=340, y=50, width=gv.inputWidth, height=gv.inputHeight)
        gv.lNameInput.place(x=340, y=75, width=gv.inputWidth, height=gv.inputHeight)
        gv.addressInput.place(x=340, y=100, width=gv.inputWidth, height=gv.inputHeight)
        gv.addressTwoInput.place(x=340, y=125, width=gv.inputWidth, height=gv.inputHeight)
        gv.cityInput.place(x=340, y=150, width=gv.inputWidth, height=gv.inputHeight)
        gv.stateInput.place(x=340, y=175, width=gv.inputWidth, height=gv.inputHeight)
        gv.zipInput.place(x=340, y=200, width=gv.inputWidth, height=gv.inputHeight)
        gv.phoneInput.place(x=340, y=225, width=gv.inputWidth, height=gv.inputHeight)
        gv.classInput.place(x=340, y=250, width=gv.inputWidth, height=gv.inputHeight)
        gv.empNumInput.place(x=340, y=275, width=gv.inputWidth, height=gv.inputHeight)
        gv.passwordInput.place(x=340, y=300, width=gv.inputWidth, height=gv.inputHeight)
        gv.departmentInput.place(x=340, y=325, width=gv.inputWidth, height=gv.inputHeight)
        gv.payRateInput.place(x=340, y=350, width=gv.inputWidth, height=gv.inputHeight)
        gv.payYTDInput.place(x=340, y=375, width=gv.inputWidth, height=gv.inputHeight)
        gv.securityInput.place(x=340, y=400, width=gv.inputWidth, height=gv.inputHeight)

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
