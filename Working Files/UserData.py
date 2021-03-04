"""
Class file to import and edit user data
"""

import pandas as pd


class UserData:

    # Load the employee csv
    def __init__(self):
        self.employee_data = pd.read_csv("employees.csv")

    # Method for setting a new password
    def change_field(self, emp_num, new_value, field):
        self.employee_data.loc[self.employee_data["id"] == emp_num, field] = new_value
        self.employee_data.to_csv("employees.csv")

    def verify_user(self, emp_num, password):
        read_password = self.employee_data.loc[self.employee_data["id"] == emp_num, "password"]

        # find the password in the gross csv data type
        for i in read_password:
            if type(i) != str:
                continue
            else:
                read_password = i

        if read_password == 'None':
            return read_password
        elif read_password == password:
            return True
        else:
            return False

    def read_value(self, emp_num, field):
        value = self.employee_data.loc[self.employee_data["id"] == emp_num, field]

        # find the value in the gross csv data type
        for i in value:
            if type(i) != str:
                continue
            else:
                value = i

        return value

    def user_exists(self, emp_num):
        # Use the users last name to see if the exist
        last_name = self.employee_data.loc[self.employee_data["id"] == emp_num, 'last_name']

        if last_name.empty:
            return False

        return True


"""
Valid fields are:
id
first_name
last_name
address
city
state
zip
classification
salary
commission
hourly
password
access
"""