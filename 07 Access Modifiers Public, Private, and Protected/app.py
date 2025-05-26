# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        #Public variable
        self._salary = salary   #Protected variable
        self.__ssn = ssn        #Private variable

emp = Employee("Zhang wei", 500000, "098-76-5432")

#Access Public variable
print("Name:", emp.name)

#Access Protected variable
print("Salary:", emp._salary)

#Access Private variable
print("SSN Private:", emp._Employee__ssn)