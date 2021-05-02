"""
Class file to save all global gui variables
"""

from tkinter import messagebox, Frame, Button, Entry, Label, StringVar, END, ANCHOR, Tk, Listbox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pandas as pd
import GlobalVariables as Globe


class GuiValues(Frame):
    """Class to HOLD EVERYTHING GUI"""
    def __init__(self, frame, controller):
        Frame.__init__(self, frame)

        # list of options for select lists
        classifications = [
            'Hourly',
            'Salary',
            'Commission',
        ]
        security_access = [
            'Admin',
            'General Manager',
            'Employee',
        ]

        self.parent = frame
        self.controller = controller
        self.count = 0

        # Create the standard for buttons
        self.button_color = '#2c71de'
        self.button_width = 20
        self.button_height = 2
        self.input_width = 380
        self.input_height = 22
        self.input_edit_color = 'white'
        self.input_read_color = 'Gray'
        self.input_border_width = 1
        self.button_text_color = "white"
        self.font_prop = ('calibre', 14, 'normal')

        # Entry variables
        self.name_var = StringVar()
        self.passw_var = StringVar()
        self.confirm_passw_var = StringVar()
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.address_var = StringVar()
        self.address2_var = StringVar()
        self.city_var = StringVar()
        self.state_var = StringVar()
        self.zip_var = StringVar()
        self.phone_var = StringVar()
        self.class_var = StringVar()
        self.emp_num_var = StringVar()
        self.department_var = StringVar()
        self.pay_rate_var = StringVar()
        self.pay_ytd_var = StringVar()
        self.security_var = StringVar()
        self.results_var = StringVar()

        # Buttons
        self.employees_button = Button(frame, text='Employees',
                                       width=self.button_width,
                                       height=self.button_height,
                                       bg=self.button_color,
                                       fg=self.button_text_color,
                                       command=lambda: self.controller.show_frame("FindEmployee"))
        self.time_cards_button = Button(frame, text='Timecards',
                                        width=self.button_width,
                                        height=self.button_height,
                                        bg=self.button_color,
                                        fg=self.button_text_color,
                                        command=lambda: self.open_new_window("Timecards"))
        self.sales_button = Button(frame, text='Sales',
                                   width=self.button_width,
                                   height=self.button_height,
                                   bg=self.button_color,
                                   fg=self.button_text_color,
                                   command=lambda: self.open_new_window("Sales"))
        self.my_profile_button = Button(frame, text='My Profile',
                                        width=self.button_width,
                                        height=self.button_height,
                                        bg=self.button_color,
                                        fg=self.button_text_color,
                                        command=self.my_profile_pressed)
        self.new_employee_button = Button(frame, text='Enter New\nEmployee',
                                          width=self.button_width,
                                          height=self.button_height,
                                          bg=self.button_color,
                                          fg=self.button_text_color,
                                          command=lambda: self.controller.show_frame("EnterNewEmployee"))
        self.find_employee_button = Button(frame, text='Find Employee',
                                           width=self.button_width,
                                           height=self.button_height,
                                           bg=self.button_color,
                                           fg=self.button_text_color,
                                           command=lambda: self.controller.show_frame("FindEmployee"))
        self.import_employee_button = Button(frame, text='Import txt of\nnew Employees',
                                             width=self.button_width,
                                             height=self.button_height,
                                             bg=self.button_color,
                                             fg=self.button_text_color,
                                             command=lambda: self.import_employees("New Employee"))
        self.save_profile_button = Button(frame, text='Save',
                                          width=self.button_width,
                                          height=self.button_height,
                                          bg=self.button_color,
                                          fg=self.button_text_color,
                                          command=lambda: self.controller.show_frame("FindEmployee"))
        self.payroll_button = Button(frame, text="Payroll",
                                     width=self.button_width,
                                     height=self.button_height,
                                     bg=self.button_color,
                                     fg=self.button_text_color,
                                     command=self.payroll_processing_refresh)
        self.login_button = Button(frame, text="Login",
                                   width=self.button_width,
                                   height=self.button_height,
                                   bg=self.button_color,
                                   fg=self.button_text_color,
                                   font=self.font_prop)
        self.create_password_button = Button(frame,
                                             text="Don't Have a Password?",
                                             width=self.button_width,
                                             height=self.button_height,
                                             bg=self.button_color,
                                             fg=self.button_text_color,
                                             font=self.font_prop,
                                             command=lambda: self.controller.show_frame("ChangePassword"))
        self.process_payroll_button = Button(frame, text='Process Payroll',
                                             width=self.button_width,
                                             height=self.button_height,
                                             bg=self.button_color,
                                             fg=self.button_text_color)
        self.import_timecard_button = Button(frame, text='Import Timecards',
                                             width=self.button_width,
                                             height=self.button_height,
                                             bg=self.button_color,
                                             fg=self.button_text_color)
        self.import_sales_button = Button(frame, text='Import Sales',
                                          width=self.button_width,
                                          height=self.button_height,
                                          bg=self.button_color,
                                          fg=self.button_text_color)
        self.set_password_button = Button(frame, text="Set Password",
                                          width=self.button_width,
                                          height=self.button_height,
                                          bg=self.button_color,
                                          fg=self.button_text_color,
                                          font=self.font_prop)
        self.cancel_button = Button(frame, text="Cancel",
                                    width=self.button_width,
                                    height=self.button_height,
                                    bg=self.button_color,
                                    fg=self.button_text_color,
                                    font=self.font_prop,
                                    command=lambda: self.controller.show_frame("LoginPage"))
        self.search_button = Button(frame, text='Search',
                                    width=self.button_width,
                                    height=self.button_height,
                                    bg=self.button_color,
                                    fg=self.button_text_color,
                                    command=self.search_pressed)
        self.edit_button = Button(frame, text='View',
                                  width=self.button_width,
                                  height=self.button_height,
                                  bg=self.button_color,
                                  fg=self.button_text_color,
                                  command=self.edit_pressed)
        self.testing = Button(frame, text='testing',
                              width=self.button_width,
                              height=self.button_height,
                              bg=self.button_color,
                              fg=self.button_text_color)
        self.refresh = Button(frame, text='Refresh',
                              width=self.button_width,
                              height=self.button_height,
                              bg=self.button_color,
                              fg=self.button_text_color)

        # Labels
        self.f_name_label = Label(frame, text="First Name:")
        self.l_name_label = Label(frame, text="Last Name:")
        self.address_label = Label(frame, text='Address:')
        self.address_line_two_label = Label(frame, text='Address Line 2:')
        self.city_label = Label(frame, text='City:')
        self.state_label = Label(frame, text='State:')
        self.zip_code_label = Label(frame, text='Zip:')
        self.phone_label = Label(frame, text='Phone Number:')
        self.classification_label = Label(frame, text='Classification:')
        self.emp_number_label = Label(frame, text='Employee Number:')
        self.password_label_user = Label(frame, text='Password:')
        self.department_label = Label(frame, text='Department:')
        self.pay_rate_label = Label(frame, text='Pay Rate:')
        self.pay_ytd_label = Label(frame, text='Pay YTD:')
        self.security_access_label = Label(frame, text='Security Access:')
        self.spacer = Label(frame, text="        ")
        self.employee_number_label = Label(frame, text="Employee Number",
                                           font=self.font_prop)
        self.password_label = Label(frame, text="Password", font=self.font_prop)
        self.payroll_desc = Label(frame, text="Will process payroll for current pay cycle")
        self.timecard_desc = Label(frame, text="Takes you to import timecards")
        self.sales_desc = Label(frame, text="Takes you to import sales reports")
        self.new_password_label = Label(frame, text="New Password",
                                        font=self.font_prop)
        self.confirm_password_label = Label(frame, text="Confirm Password",
                                            font=self.font_prop)
        self.results_label = Label(frame, text="Results:")

        # Inputs
        self.f_name_input = Entry(frame, textvariable=self.fname_var,
                                  bg=self.input_edit_color,
                                  borderwidth=self.input_border_width)
        self.l_name_input = Entry(frame, textvariable=self.lname_var,
                                  bg=self.input_edit_color,
                                  borderwidth=self.input_border_width)
        self.address_input = Entry(frame, textvariable=self.address_var,
                                   bg=self.input_edit_color,
                                   borderwidth=self.input_border_width)
        self.address_two_input = Entry(frame, textvariable=self.address2_var,
                                       bg=self.input_edit_color,
                                       borderwidth=self.input_border_width)
        self.city_input = Entry(frame, textvariable=self.city_var,
                                bg=self.input_edit_color,
                                borderwidth=self.input_border_width)
        self.state_input = Entry(frame, textvariable=self.state_var,
                                 bg=self.input_edit_color,
                                 borderwidth=self.input_border_width)
        self.zip_input = Entry(frame, textvariable=self.zip_var,
                               bg=self.input_edit_color,
                               borderwidth=self.input_border_width)
        self.phone_input = Entry(frame, textvariable=self.phone_var,
                                 bg=self.input_edit_color,
                                 borderwidth=self.input_border_width)
        self.class_input = Entry(frame, textvariable=self.class_var,
                                 bg=self.input_edit_color,
                                 borderwidth=self.input_border_width)
        self.emp_num_input = Entry(frame, textvariable=self.emp_num_var,
                                   bg=self.input_edit_color,
                                   borderwidth=self.input_border_width)
        self.password_input = Entry(frame, textvariable=self.passw_var,
                                    bg=self.input_edit_color,
                                    borderwidth=self.input_border_width)
        self.department_input = Entry(frame, textvariable=self.department_var,
                                      bg=self.input_edit_color,
                                      borderwidth=self.input_border_width)
        self.pay_rate_input = Entry(frame, textvariable=self.pay_rate_var,
                                    bg=self.input_edit_color,
                                    borderwidth=self.input_border_width)
        self.pay_ytd_input = Entry(frame, textvariable=self.pay_ytd_var,
                                   bg=self.input_edit_color,
                                   borderwidth=self.input_border_width)
        self.security_input = Entry(frame, textvariable=self.security_var,
                                    bg=self.input_edit_color,
                                    borderwidth=self.input_border_width)
        self.user_entry = Entry(frame, textvariable=self.name_var,
                                font=self.font_prop)
        self.password_entry = Entry(frame, textvariable=self.passw_var,
                                    show="*",
                                    font=self.font_prop)
        self.set_password_entry = Entry(frame, textvariable=self.passw_var,
                                        show="*",
                                        font=self.font_prop)
        self.confirm_password_entry = Entry(frame,
                                            textvariable=self.confirm_passw_var,
                                            show="*",
                                            font=self.font_prop)
        self.results_entry = Listbox(frame, bg=self.input_edit_color,
                                     borderwidth=self.input_border_width)

    def create_nav_bar(self):
        """Class to create the navbar for eachpage"""
        if Globe.EMPACCESS == 1:
            self.employees_button.place(x=0, y=0)
            self.time_cards_button.place(x=185, y=0)
            self.sales_button.place(x=370, y=0)
            self.payroll_button.place(x=555, y=0)
            self.my_profile_button.place(x=740, y=0)
        else:
            self.employees_button.place(x=0, y=0)
            self.my_profile_button.place(x=185, y=0)

    def my_profile_values(self):
        """Method for filling the values on My Profile"""
        emp_id = Globe.Pr.current_emp
        user = Globe.Pr.get_profile(emp_id)

        # Clear all fields in case of double click
        self.f_name_input.delete(0, "end")
        self.f_name_input.delete(0, "end")
        self.l_name_input.delete(0, "end")
        self.address_input.delete(0, "end")
        self.address_two_input.delete(0, "end")
        self.city_input.delete(0, "end")
        self.state_input.delete(0, "end")
        self.zip_input.delete(0, "end")
        self.phone_input.delete(0, "end")
        self.class_input.delete(0, "end")
        self.emp_num_input.delete(0, "end")
        self.password_input.delete(0, "end")
        self.department_input.delete(0, "end")
        self.pay_rate_input.delete(0, "end")
        self.pay_ytd_input.delete(0, "end")
        self.security_input.delete(0, "end")

        # Insert values from CSV
        self.f_name_input.insert(0, user[1])
        self.l_name_input.insert(0, user[2])
        self.address_input.insert(0, user[3])
        self.address_two_input.insert(0, user[4])
        self.city_input.insert(0, user[5])
        self.state_input.insert(0, user[6])
        self.zip_input.insert(0, user[7])
        self.phone_input.insert(0, user[14])
        self.class_input.insert(0, user[8])
        self.emp_num_input.insert(0, user[0])
        self.password_input.insert(0, user[12])
        self.department_input.insert(0, user[15])
        self.pay_rate_input.insert(0, user[11])
        self.pay_ytd_input.insert(0, user[9])
        self.security_input.insert(0, user[13])

    def open_new_window(self, title):
        """Pop up for importing files"""
        master = Tk()

        master.geometry("800x300")

        master.title(title)

        type_label = Label(master, text=title + " file must be a .txt or .csv file.")
        file_input_label = Label(master, text="File for import:")
        input_field = Entry(master,
                            bg=self.input_edit_color,
                            state='disabled',
                            width=50)
        upload_button = Button(master, text="Upload",
                               width=self.button_width,
                               bg=self.button_color,
                               fg=self.button_text_color,
                               height=self.button_height,
                               command=lambda: [input_field.config(state='normal'),
                                                input_field.delete(0, END),
                                                input_field.insert(0, self.get_file_name()),
                                                input_field.config(state='readonly')])
        submit_button = Button(master, text="Submit",
                               width=self.button_width,
                               bg=self.button_color,
                               fg=self.button_text_color,
                               height=self.button_height,
                               command=lambda: [self.upload_file(input_field.get(), title),
                                                master.destroy(),
                                                self.payroll_processing_refresh()])

        type_label.place(x=100, y=50)
        file_input_label.place(x=100, y=100)
        input_field.place(x=200, y=100)
        upload_button.place(x=100, y=150)
        submit_button.place(x=400, y=150)

    def import_employees(self, title):
        """Pop up for importing employees file"""
        master = Tk()

        master.geometry("800x300")

        master.title(title)

        type_label = Label(master, text=title + " file must be a .txt or .csv file.")
        file_input_label = Label(master, text="File for import:")
        input_field = Entry(master,
                            bg=self.input_edit_color,
                            state='disabled',
                            width=50)
        upload_button = Button(master, text="Locate File",
                               width=self.button_width,
                               bg=self.button_color,
                               fg=self.button_text_color,
                               height=self.button_height,
                               command=lambda: [input_field.config(state='normal'),
                                                input_field.delete(0, END),
                                                input_field.insert(0, self.set_file_name()),
                                                input_field.config(state='readonly')])
        submit_button = Button(master, text="Submit",
                               width=self.button_width,
                               bg=self.button_color,
                               fg=self.button_text_color,
                               height=self.button_height,
                               command=lambda: [Globe.Pr.new_employees(input_field.get()),
                                                master.destroy()])

        type_label.place(x=100, y=50)
        file_input_label.place(x=100, y=100)
        input_field.place(x=200, y=100)
        upload_button.place(x=100, y=150)
        submit_button.place(x=400, y=150)

    def save_log(self, title):
        """Pop up for importing employees file"""
        master = Tk()

        master.geometry("800x300")

        master.title(title)

        type_label = Label(master, text=f"Where would you like to save your {title}?")
        file_input_label = Label(master, text="Location to save log:")
        input_field = Entry(master,
                            bg=self.input_edit_color,
                            state='disabled',
                            width=50)
        upload_button = Button(master, text="Set Location",
                               width=self.button_width,
                               bg=self.button_color,
                               fg=self.button_text_color,
                               height=self.button_height,
                               command=lambda: [input_field.config(state='normal'),
                                                input_field.delete(0, END),
                                                input_field.insert(0, self.set_file_name()),
                                                input_field.config(state='readonly')])
        submit_button = Button(master, text="Submit",
                               width=self.button_width,
                               bg=self.button_color,
                               fg=self.button_text_color,
                               height=self.button_height,
                               command=lambda: [self.assign_file(input_field.get()), master.destroy()])

        type_label.place(x=100, y=45)
        file_input_label.place(x=100, y=100)
        input_field.place(x=230, y=100)
        upload_button.place(x=100, y=150)
        submit_button.place(x=400, y=150)

    def assign_file(self, new_file):
        Globe.Pr.pay_logfile = new_file
        # Process Payroll
        try:
            Globe.Pr.run_payroll()
            messagebox.showinfo("Success!", "Payroll was Successfully Processed.")
        except Exception as error:
            messagebox.showinfo("Error!", f"There was an Error in Processing Payroll! "
                                          f"Please Contact your Administrator: {error}")

        # Reset the values and refresh the page
        Globe.timecards_file = None
        Globe.sales_file = None
        self.payroll_processing_refresh()

    @staticmethod
    def get_file_name():
        """Method to get the file name of the uploaded file"""
        return askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])

    @staticmethod
    def set_file_name():
        """Method to set and save the log file"""
        return asksaveasfilename(defaultextension='.txt',
                                 initialfile="Paylog.txt")

    @staticmethod
    def upload_file(file_path, file_type):
        """Method to read the uploaded file"""
        try:
            uploaded_file = pd.read_csv(file_path)
            if file_type == 'Timecards':
                Globe.timecards_file = uploaded_file
                # print(Globe.timecardsFile)
            else:
                Globe.sales_file = uploaded_file
                # print(Globe.salesFile)

            # print('fp', filePath)
            # print('hi', uploadedFile)
        except:
            messagebox.showerror("Error!", "There was an error submitting the file")

    def search_pressed(self):
        """Method to invoke search when the button is pressed"""
        search_number = self.emp_num_input.get()
        search_f_name = self.f_name_input.get()
        search_l_name = self.l_name_input.get()
        search_phone = self.phone_input.get()

        results = []
        results.clear()
        self.results_entry.delete(0, END)

        if search_number != '':
            first_name = Globe.ud.read_value(search_number, 'first_name')
            last_name = Globe.ud.read_value(search_number, 'last_name')
            user_department = Globe.ud.read_value(search_number, 'department')

            results.append(last_name + ', ' + first_name + ' Dept:' +
                           user_department + ' id:' + search_number)

        elif search_f_name != '':
            first_name_results = Globe.ud.get_match(search_f_name)
            for person in first_name_results:
                first_name = Globe.ud.read_value(person, 'first_name')
                last_name = Globe.ud.read_value(person, 'last_name')
                user_department = Globe.ud.read_value(person, 'department')

                results.append(last_name + ', ' + first_name + ' Dept:' +
                               user_department + ' id:' + person)

        elif search_l_name != '':
            last_name_results = Globe.ud.get_match('', search_l_name)
            for person in last_name_results:
                first_name = Globe.ud.read_value(person, 'first_name')
                last_name = Globe.ud.read_value(person, 'last_name')
                user_department = Globe.ud.read_value(person, 'department')

                results.append(last_name + ', ' + first_name + ' Dept:' +
                               user_department + ' id:' + person)

        elif search_phone != '':
            phone_number_results = Globe.ud.get_match('', '', search_phone)
            for person in phone_number_results:
                first_name = Globe.ud.read_value(person, 'first_name')
                last_name = Globe.ud.read_value(person, 'last_name')
                user_department = Globe.ud.read_value(person, 'department')

                results.append(last_name + ', ' + first_name + ' Dept:' +
                               user_department + ' id:' + person)
        else:
            messagebox.showwarning('No Values Entered',
                                   'You must enter a value in one of the search boxes to get a search result.')

        results.sort()
        if len(results) == 0:
            results.append('No results found')

        for item in results:
            self.results_entry.insert(END, item)

    def set_anchor(self, selected=None):
        Globe.ANCHOR = self.results_entry.get(ANCHOR)

    def edit_pressed(self):
        # self.controller.show_frame("EditEmployee")
        # self.edit_profile_values()
        if self.results_entry.get(ANCHOR) != '':
            open_this = self.results_entry.get(ANCHOR)
            ind_id = open_this.index('id:')
            ind_id += 3
            search_id = open_this[ind_id:]
            user = Globe.Pr.get_profile(search_id)
            Globe.search_result = user

        self.edit_refresh()

    def payroll_processing_refresh(self):
        """Method to refresh payroll processing when files are uploaded"""
        self.controller.replace_payroll_processing()
        self.controller.show_frame("PayrollProcessing")

    def edit_refresh(self):
        """Method to refresh the edit page to fill in the values of the search result"""
        self.controller.replace_edit_employee()
        self.controller.show_frame("EditEmployee")

    def my_profile_pressed(self):
        """Method to refresh my profile when it's pressed"""
        self.controller.replace_my_profile()
        self.controller.show_frame("MyProfile")
