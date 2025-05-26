# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object
# store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name
        print(f"Employee created: {self.name}")
        
class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []
        print(f"Department created: {self.dept_name}")
        
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.dept_name}")

emp1 = Employee("Ali")
emp2 = Employee("Hoor")
dept = Department("HR")
dept.add_employee(emp1)
dept.add_employee(emp2)