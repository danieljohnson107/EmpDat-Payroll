"""
Class file to save all global gui variables
"""

from tkinter import *


class GuiValues:

    def __init__(self):

        # Create the standard for buttons
        self.buttonColor = '#2c71de'
        self.buttonWidth = 20
        self.buttonHeight = 2
        self.inputWidth = 380
        self.inputHeight = 22
        self.inputEditColor = 'white'
        self.inputReadColor = 'Gray'
        self.inputBorderWidth = 1
        self.buttonTextColor = "white"
        self.fontProp = ('calibre', 14, 'normal')

    # Create nav bar stuff here so we don't need it in EVERY file
    def create_button(self, frame, new_state="normal", function=None, new_text="Error"):
        return Button(frame, text=new_text, width=self.buttonWidth, bg=self.buttonColor, height=self.buttonHeight,
                      fg=self.buttonTextColor, state=new_state, command=function)
