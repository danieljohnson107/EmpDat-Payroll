"""
Trying to implement stacked frames into our program
"""

from FindEmployee import *
from PayrollProcessing import *
from MyProfile import *
from EnterNewEmployee import *

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


if __name__ == "__main__":
    app = App()
    app.mainloop()
