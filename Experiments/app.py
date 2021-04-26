"""
Trying to implement stacked frames into our program
"""

from tkinter import Frame, Tk
from FindEmployee import FindEmployee
from PayrollProcessing import PayrollProcessing
from MyProfile import MyProfile
from EnterNewEmployee import EnterNewEmployee
from EditEmployee import EditEmployee


class App(Tk):
    """Primary app class to run all frames but the login frames"""

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
        for page in (FindEmployee, PayrollProcessing,
                  MyProfile, EnterNewEmployee, EditEmployee):
            page_name = page.__name__
            frame = page(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("FindEmployee")

    def show_frame(self, page_name):
        """Method to call and change the frame """
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == 'EditEmployee':
            frame.after(200, frame.update())

    def replace_payroll_processing(self):
        """Method to refresh payroll processing so that the button may be used"""
        # Refresh the page when values are changed
        page_name = PayrollProcessing.__name__
        frame = PayrollProcessing(parent=self.container, controller=self)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

    def replace_edit_employee(self):
        """Method to refresh the EditEmployee Page so that the selected employees data is shown"""
        # Refresh the page when values are changed
        page_name = EditEmployee.__name__
        frame = EditEmployee(parent=self.container, controller=self)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

    def replace_my_profile(self):
        """Method to refresh my_profile data"""
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
