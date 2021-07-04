# https://realpython.com/inheritance-composition-python/
# Modeling HR System

class Employee:
    # Base class Employee
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    # SalaryEmployee inherits from base class Employee
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def calculate_payroll(self):
        return self.salary


class ComissionEmployee(SalaryEmployee):
    # Inherits Salary Employee since they do
    # receive salary but with extra comission
    def __init__(self, id, name, salary, comission):
        super().__init__(id, name, salary)
        self.comission = comission

    def calculate_payroll(self):
        fixed_income = super().calculate_payroll()
        return fixed_income + self.comission


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.hours_worked


class PayrollSystem:
    def calculate_payroll(self, employees: Employee):
        print("Calculating payroll...")
        for employee in employees:
            print(f"${employee.id} - ${employee.name}")
            print(f"Amount: ${employee.calculate_payroll()}")
            print("FINISHED")


sam = ComissionEmployee(111, "Sam", 20000, 5000)
print(sam.calculate_payroll())
