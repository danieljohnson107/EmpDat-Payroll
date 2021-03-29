from abc import ABC, abstractmethod
import os, os.path

PAY_LOGFILE = "paylog.txt"

employees = []


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


def authenticate(emp_id, password):
    # Find the proper employee object
    for i in employees:
        if i.emp_id == emp_id:
            # Make sure the password isn't blank
            if i.password == "None":
                return i.password

            # Check the password
            if i.password == password:
                return True
            else:
                return False
        else:
            pass


def user_exists(emp_id):
    # Check to see if the employee exists
    for i in employees:
        if i.emp_id == emp_id:
            return True

    return False


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
        self.password = password
        self.access = access
        self.phone_number = phone_number
        self.department = department
        if classification == 1:
            self.classification = Salaried(salary)
        elif classification == 2:
            self.classification = Commissioned(salary, commission)
        else:
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