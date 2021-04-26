"""
Payroll Processing Excellence main file
"""
from tkinter import Tk, Frame
from ChangePassword import ChangePassword
from LoginPage import LoginPage


class PayrollProcessingExcellence(Tk):
    """Main file for Logging in and Starting the program"""
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("925x500")
        self.title('Payroll Processing Excellence: Team 5')

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ChangePassword, LoginPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        """Method to change frames"""
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = PayrollProcessingExcellence()
    app.mainloop()
