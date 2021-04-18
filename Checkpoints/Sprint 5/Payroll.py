from abc import ABC, abstractmethod
import os, os.path

PAY_LOGFILE = "paylog.txt"

employees = []
global current_emp


def load_employees():
    """Loads employee data into memory and creates an instance of the employee object for each entry"""
    with open("employees.csv", "r") as emp_file:
        first_line = True
        for line in emp_file:
            if first_line:
                first_line = False
                continue
            tmp = line[:-1].split(",")
            employees.append(Employee(tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], int(tmp[8]), int(tmp[9]),
                                      float(tmp[10]), float(tmp[11]), float(tmp[12]), tmp[13], int(tmp[14]),
                                      tmp[15], tmp[16]))

    # Create the .old file at the same time
    old = open("employees.csv.old", "w")
    for i in employees:
        old.write(f"0,"
                  f"{i.emp_id},"
                  f"{i.first_name},"
                  f"{i.last_name},"
                  f"{i.address},"
                  f"{i.address2},"
                  f"{i.city},"
                  f"{i.state},"
                  f"{i.postal_code},"
                  f"{class_number(i.class_text)},"
                  f"{i.salary},"
                  f"{i.commission},"
                  f"{i.hourly},"
                  f"{i.password},"
                  f"{i.access},"
                  f"{i.phone_number},"
                  f"{i.department}\n")

    # Close the files
    old.close()


def authenticate(emp_id, password):
    global current_emp
    current_emp = emp_id

    employee = find_employee_by_id(emp_id)

    # Make sure the password isn't blank
    if employee.password == "None":
        return employee.password

    # Check the password
    if employee.password == password:
        return True
    else:
        return False


def user_exists(emp_id):
    # Check to see if the employee exists
    for i in employees:
        if i.emp_id == emp_id:
            return True

    return False


def change_password(emp_id, value):
    """ Function to verify and set a new password """
    employee = find_employee_by_id(emp_id)

    if employee.password != "None":
        return False

    chars = 0
    ints = 0
    spec = 0
    upper = 0
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "?", "_", "=", ",", "<", ">", "/", "'",
                     '"', " "]

    # Grab the total amount of each value
    for i in value:
        try:
            int(i)
            ints += 1
        except ValueError:
            if i in special_chars:
                spec += 1
            else:
                chars += 1

                # Check for upper case
                if i.isupper():
                    upper += 1

    if len(value) >= 8 and upper >= 1 and spec >= 1 and ints >= 1:
        employee.password = value
        write_out()
        return True
    else:
        return "Fail"


def process_timecards():
    """Processes time cards for hourly employees"""
    with open("timecards.csv", "r") as time_file:
        for line in time_file:
            emp_time = line[:-1].split(",")
            emp = find_employee_by_id(emp_time[0])
            if isinstance(emp.classification, Hourly):
                for hours in emp_time[1:]:
                    emp.classification.add_timecard(float(hours))


def process_receipts():
    """Processes reciepts for commissioned employees"""
    with open("receipts.csv", "r") as receipts_file:
        for line in receipts_file:
            emp_receipts = line[:-1].split(",")
            emp = find_employee_by_id(emp_receipts[0])
            if isinstance(emp.classification, Commissioned):
                for receipt in emp_receipts[1:]:
                    emp.classification.add_receipt(float(receipt))


def run_payroll():
    """Runs payroll for all employees"""
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘payroll.txt’
        os.remove(PAY_LOGFILE)
    for emp in employees:   # employees is the global list of Employee objects
        emp.issue_payment() # issue_payment calls a method in the classification
                            # object to compute the pay, which in turn invokes
                            # the pay method.


def find_employee_by_id(id):
    for employee in employees:
        if employee.emp_id == id:
            return employee

    return False


def get_profile(emp_id):

    i = find_employee_by_id(emp_id)

    data = [i.emp_id, i.first_name, i.last_name, i.address, i.address2, i.city, i.state, i.postal_code, i.class_text,
            i.salary, i.commission, i.hourly, i.password, i.access, i.phone_number, i.department]

    # Check the data for any none values
    for i in range(len(data)):
        if data[i] == 'nan':
            data[i] = ""

    return data


def save_profile(emp_id, first_name, last_name, address, address2, city, state, postal_code, classification, salary,
                 hourly, password, access, phone_number, department):

    employee = find_employee_by_id(emp_id)

    try:
        # assign the values to the array
        employee.emp_id = emp_id
        employee.first_name = first_name
        employee.last_name = last_name
        employee.address = address
        employee.address2 = address2
        employee.city = city
        employee.state = state
        employee.postal_code = postal_code
        employee.classification = classification
        employee.salary = salary
        employee.hourly = hourly
        employee.password = password
        employee.access = access
        employee.phone_number = phone_number
        employee.department = department

        # Get a text version of the classification
        if classification == 1:
            employee.class_text = "Salaried"
        elif classification == 2:
            employee.class_text = "Commissioned"
        else:
            employee.class_text = "Hourly"

        write_out()

        return True
    except:
        return False


def new_user(emp_id, first_name, last_name, address, address2, city, state, postal_code, classification, salary,
             hourly, password, access, phone_number, department, commission=""):

    new_employee = Employee(emp_id, first_name, last_name, address, address2, city, state, postal_code, classification,
                            salary, commission, hourly, password, access, phone_number, department)

    employees.append(new_employee)
    write_out()


def write_out():
    """ Function to write all user data to employees.csv """
    with open("employees.csv", "w") as new_data:
        new_data.write(",id,first_name,last_name,address,address2,city,state,zip,classification,salary,commission,"
                       "hourly,password,access,phone_number,department\n")
        for i in employees:
            new_data.write(f"0,"
                           f"{i.emp_id},"
                           f"{i.first_name},"
                           f"{i.last_name},"
                           f"{i.address},"
                           f"{i.address2},"
                           f"{i.city},"
                           f"{i.state},"
                           f"{i.postal_code},"
                           f"{class_number(i.class_text)},"
                           f"{i.salary},"
                           f"{i.commission},"
                           f"{i.hourly},"
                           f"{i.password},"
                           f"{i.access},"
                           f"{i.phone_number},"
                           f"{i.department}\n")


def class_number(classification):
    if classification == "Salaried":
        return "1"
    elif classification == "Commissioned":
        return "2"
    else:
        return "3"

class Employee:
    """Defines an Employee object
    Required Params: emp_id, first_name, last_name, address, address2, city, state, postal_code, classification, salary,
    commission, hourly, password, access, phone_number, department
    """
    def __init__(self, emp_id, first_name, last_name, address, address2, city, state, postal_code, classification,
                 salary, commission, hourly, password, access, phone_number, department):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.address2 = address2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.classification = classification
        self.class_text = ""
        self.salary = salary
        self.commission = commission
        self.hourly = hourly
        self.password = password
        self.access = access
        self.phone_number = phone_number
        self.department = department
        if classification == 1:
            self.class_text = "Salaried"
            self.classification = Salaried(salary)
        elif classification == 2:
            self.class_text = "Commissioned"
            self.classification = Commissioned(salary, commission)
        else:
            self.class_text = "Hourly"
            self.classification = Hourly(hourly)
    
    def make_hourly(self, hourly_rate):
        """Sets the Employee classification to hourly"""
        self.classification = Hourly(hourly_rate)

    def make_salaried(self, salary):
        """Sets the Employee classification to salaried"""
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, commission_rate):
        """Sets the Employee classification to commissioned"""
        self.classification = Commissioned(salary, commission_rate)

    def issue_payment(self):
        """Issues payment to employee"""
        pay = self.classification.compute_pay()
        if pay > 0:
            with open(PAY_LOGFILE, "a") as paylog:
                print("Mailing", f"{pay:.2f}", "to", self.first_name, self.last_name,
                "at", self.address, self.city, self.state, self.postal_code, file=paylog)


class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        pass


class Hourly(Classification):
    """Defines methods for hourly Employees"""
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecard = []

    def add_timecard(self, hours):
        self.timecard.append(hours)

    def compute_pay(self):
        pay = round(sum(self.timecard)*self.hourly_rate, 2)
        self.timecard.clear()
        return pay


class Salaried(Classification):
    """Defines methods for salaried Employees"""
    def __init__(self, salary):
        self.salary = salary
    
    def compute_pay(self):
        return round(self.salary/24, 2)


class Commissioned(Salaried):
    """Defines methods for commissioned Employees"""
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def add_receipt(self, amount):
        self.receipts.append(amount)

    def compute_pay(self):
        pay = round((sum(self.receipts)*self.commission_rate/100)+self.salary/24, 2)
        self.receipts.clear()
        return pay