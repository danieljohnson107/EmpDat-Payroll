"""
Class file to import and edit user data
"""

import pandas as pd


class UserData:

    # Load the employee csv
    def __init__(self):
        self.employee_data = pd.read_csv("employees.csv", index_col=0)
        self.employee_number = ""
        self.columns = ["id", "first_name", "last_name", "address", "address2", "city", "state", "zip", "classification"
                        , "salary", "commission", "hourly", "password", "access", "phone_number", "department"]

    # Method for setting a new password
    def change_field(self, emp_num, new_value, field):
        self.employee_data.loc[self.employee_data["id"] == emp_num, field] = new_value
        self.employee_data.to_csv("employees.csv")
        return True

    def verify_user(self, emp_num, password):
        read_password = self.employee_data.loc[self.employee_data["id"] == emp_num, "password"]

        # find the password in the gross csv data type
        for i in read_password:
            if type(i) != str:
                continue
            else:
                read_password = i

        # assign the employee number
        self.employee_number = emp_num

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
            if type(i) != str and i < 10 and i not in [1, 2, 3]:
                continue
            else:
                value = str(i)

        return value

    def get_match(self, firstName=None, lastName=None, phoneNumber=None):
        matchs = []
        if lastName is not None:
            for num in self.employee_data.id:
                match = self.read_value(num, 'last_name')
                if lastName.lower() in match.lower():
                    matchs.append(num)
        elif firstName is not None:
            for num in self.employee_data.id:
                match = self.read_value(num, 'first_name')
                if firstName.lower() in match.lower():
                    matchs.append(num)
        elif phoneNumber is not None:
            for num in self.employee_data.id:
                match = self.read_value(num, 'phone_number')
                if phoneNumber.lower() in match.lower():
                    matchs.append(num)
        return matchs

    def user_exists(self, emp_num):
        # Use the users last name to see if the exist
        last_name = self.employee_data.loc[self.employee_data["id"] == emp_num, 'last_name']

        if last_name is None:
            return False

        return True

    def new_user(self, user_data):
        new_user = pd.DataFrame(columns=self.columns)

        # Make sure the id doesn't exist or just assign it a number (You get no choice)

        # Set the new values
        new_user.loc[0, 'id'] = user_data[0]
        new_user.loc[new_user["id"] == user_data[0], 'first_name'] = user_data[1]
        new_user.loc[new_user["id"] == user_data[0], 'last_name'] = user_data[2]
        new_user.loc[new_user["id"] == user_data[0], 'address'] = user_data[3]
        new_user.loc[new_user["id"] == user_data[0], 'address2'] = user_data[4]
        new_user.loc[new_user["id"] == user_data[0], 'city'] = user_data[5]
        new_user.loc[new_user["id"] == user_data[0], 'state'] = user_data[6]
        new_user.loc[new_user["id"] == user_data[0], 'zip'] = user_data[7]
        new_user.loc[new_user["id"] == user_data[0], 'phone_number'] = user_data[8]
        new_user.loc[new_user["id"] == user_data[0], 'classification'] = user_data[9]
        new_user.loc[new_user["id"] == user_data[0], 'password'] = user_data[10]
        new_user.loc[new_user["id"] == user_data[0], 'department'] = user_data[11]
        new_user.loc[new_user["id"] == user_data[0], 'hourly'] = user_data[12]
        new_user.loc[new_user["id"] == user_data[0], 'salary'] = user_data[13]
        new_user.loc[new_user["id"] == user_data[0], 'access'] = user_data[14]

        # Append to csv
        new_user.to_csv('employees.csv', mode='a', header=False)

        # Reload the dataframe
        self.employee_data = pd.read_csv("employees.csv", index_col=0)


"""
Valid fields are:
id
first_name
last_name
address
address2
city
state
zip
classification
salary
commission
hourly
password
access
phone_number
department
"""
