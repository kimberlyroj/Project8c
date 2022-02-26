# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/25/2022
# Description: A class named Employee that has private data members for an employee's name, ID_number, salary, and email_address
class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        self.__name = name
        self.__ID = ID_number
        self.__salary = salary
        self.__email_address = email_address
    def get_name(self):
        return self.__name
    def get_ID_number(self):
        return self.__ID
    def get_salary(self):
        return self.__salary
    def get_email_address(self):
        return self.__email_address

def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    employees = dict()
    for i in range(len(emp_names)):
        employees[emp_ids[i]] = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i])
    return employees

emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)

for emp in result:
    print(emp, result[emp])