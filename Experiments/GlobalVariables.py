"""
Method for handling global variables saved in a JSON file
"""
import json
from UserData import UserData
import Payroll as Pr

# Declare variables that can be accessed anywhere
ud = UserData()
sales_file = None
timecards_file = None
EMPACCESS = None
ANCHOR = ''
search_result = ''

# Load the employees
Pr.load_employees()


class GlobalVariables:
    """Class to store global variables in a JSON"""
    # Path to the file
    FILE = "JSON/Global.json"

    # Empty Initialization
    def __init__(self):
        return

    def open(self):
        """Method to open the file"""
        # Open the json file specifying utf-8 just in case
        json_file = open(self.FILE, "r")

        # Check to see if the file has something in it or return prematurely
        if json_file.read() == '' or json_file.read() is None:
            return None

        # Load the json data and assign it to global_vars
        with open(self.FILE) as file:
            global_vars = json.load(file)

        # Close the json file
        json_file.close()

        # Convert the json data to a dict
        global_vars = json.loads(global_vars)

        # Return the global variables to the caller
        return global_vars

    def close(self, new_dict):
        """Method to save the files"""
        # Open the json file with write privileges
        json_file = open(self.FILE, "w")

        # convert dict to json
        convert = json.dumps(new_dict)

        # Writing to the file also clears it so write the new data to the file
        json.dump(convert, json_file)

        # Close the json file
        json_file.close()
