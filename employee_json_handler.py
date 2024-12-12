import json
from employee import Employee, Language

class EmployeeJSONHandler:
    FILE_PATH = 'employees.json'

    @staticmethod
    def read_employees():
        try:
            with open(EmployeeJSONHandler.FILE_PATH, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_employees(employees):
        with open(EmployeeJSONHandler.FILE_PATH, 'w') as file:
            json.dump(employees, file, indent=4)

    @staticmethod
    def add_employee(employee):
        employees = EmployeeJSONHandler.read_employees()
        employees.append(employee.to_dict())
        EmployeeJSONHandler.save_employees(employees)

    @staticmethod
    def search_employee(search_term):
        employees = EmployeeJSONHandler.read_employees()
        results = []
        for emp in employees:
            if str(emp['EmployeeID']) == search_term or emp['Designation'].lower() == search_term.lower():
                results.append(emp)
        return results

    @staticmethod
    def delete_employee(employee_id):
        employees = EmployeeJSONHandler.read_employees()
        employees = [emp for emp in employees if emp['EmployeeID'] != employee_id]
        EmployeeJSONHandler.save_employees(employees)
