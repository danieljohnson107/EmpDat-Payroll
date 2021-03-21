"""
Method for handling global variables saved in a JSON file
"""
import json
from UserData import *

# Declare variables that can be accessed anywhere
ud = UserData()
salesFile = None
timecardsFile = None


class GlobalVariables:

    # Path to the file
    FILE = "JSON/Global.json"

    # Empty Initialization
    def __init__(self):
        return

    # Open method used for initially importing global variables
    def open(self):
        # Open the json file specifying utf-8 just in case
        json_file = open(self.FILE, "r")

        # Check to see if the file has something in it or return prematurely
        if json_file.read() == '' or json_file.read() is None:
            return

        # Load the json data and assign it to global_vars
        with open(self.FILE) as f:
            global_vars = json.load(f)

        # Close the json file
        json_file.close()

        # Convert the json data to a dict
        global_vars = json.loads(global_vars)

        # Return the global variables to the caller
        return global_vars

    # Closing method to save any global variables that have been changed
    def close(self, new_dict):

        # Open the json file with write privileges
        json_file = open(self.FILE, "w")

        # convert dict to json
        convert = json.dumps(new_dict)

        # Writing to the file also clears it so write the new data to the file
        json.dump(convert, json_file)

        # Close the json file
        json_file.close()
