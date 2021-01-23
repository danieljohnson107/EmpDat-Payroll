from abc import ABC, abstractmethod
import os, os.path

PAY_LOGFILE = "paylog.txt"

employees = []
def load_employees():
    with open("employees.csv", "r") as emp_file:
        first_line = True
        for line in emp_file:
            if first_line:
                first_line = False
                continue
            tmp = line[:-1].split(",")
            employees.append(Employee(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6],int(tmp[7]),float(tmp[8]),float(tmp[9]),float(tmp[10])))

def process_timecards():
    with open("timecards.csv", "r") as time_file:
        for line in time_file:
            emp_time = line[:-1].split(",")
            emp = find_employee_by_id(emp_time[0])
            if isinstance(emp.classification, Hourly):
                for hours in emp_time[1:]:
                    emp.classification.add_timecard(float(hours))

def process_receipts():
    with open("receipts.csv", "r") as receipts_file:
        for line in receipts_file:
            emp_receipts = line[:-1].split(",")
            emp = find_employee_by_id(emp_receipts[0])
            if isinstance(emp.classification, Commissioned):
                for receipt in emp_receipts[1:]:
                    emp.classification.add_receipt(float(receipt))

def run_payroll():
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

class Employee():
    def __init__(self, emp_id, first_name, last_name, address, city, state, postal_code, classification, salary, commission, hourly):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        if classification == 1:
            self.classification = Salaried(salary)
        elif classification ==2:
            self.classification = Commissioned(salary, commission)
        else:
            self.classification = Hourly(hourly)
    
    def make_hourly(self, hourly_rate):
        self.classification = Hourly(hourly_rate)

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, commission_rate):
        self.classification = Commissioned(salary, commission_rate)

    def issue_payment(self):
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
    def __init__(self, salary):
        self.salary = salary
    
    def compute_pay(self):
        return round(self.salary/24, 2)

class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def add_receipt(self, ammount):
        self.receipts.append(ammount)

    def compute_pay(self):
        pay = round((sum(self.receipts)*self.commission_rate/100)+self.salary/24, 2)
        self.receipts.clear()
        return pay