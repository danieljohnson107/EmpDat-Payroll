"""
Trying to implement stacked frames into our program
"""

from FindEmployee import *
from PayrollProcessing import *
from MyProfile import *
from EnterNewEmployee import *
from EditEmployee import *
from tkinter import *

global frame


class App(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("925x500")
        self.title('Payroll Processing Excellence: Team 5')

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.container = container

        self.frames = {}
        for F in (FindEmployee, PayrollProcessing,
                  MyProfile, EnterNewEmployee, EditEmployee):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("FindEmployee")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == 'EditEmployee':
            frame.after(200, frame.update())

    def replace_PayrollProcessing(self):
        # Refresh the page when values are changed
        page_name = PayrollProcessing.__name__
        frame = PayrollProcessing(parent=self.container, controller=self)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

    def replace_EditEmployee(self):
        # Refresh the page when values are changed
        page_name = EditEmployee.__name__
        frame = EditEmployee(parent=self.container, controller=self)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

    def replace_my_profile(self):
        # Refresh the page when values are changed
        page_name = MyProfile.__name__
        frame = MyProfile(parent=self.container, controller=self)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
