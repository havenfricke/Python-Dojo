from Person import Person        # A parent class must be imported to be extended or inherited (from FileName import ClassName)
import re                        # import re for access to .match() method

class Employee(Person):
    def __init__(self, name, age, email, phoneNumber, role, employee_id, salary):         # super().__init__() calls the constructor of the parent 'Person' class.
        super().__init__(name, age, email, phoneNumber, role)                             # This automatically runs the validation logic in the parent's setters.
        self.employee_id = employee_id                                    # Initialize the new attributes specific to Employee
        self.salary = salary


    # Employee ID
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        id_regex = r"^EMP-\d{4}$"                                         # Example regex validation: ID must start with 'EMP-' followed by 4 digits
        if not re.match(id_regex, value):
            raise ValueError(f"Invalid ID format. Expected EMP-XXXX, got '{value}'")
        self._employee_id = value


    # Salary
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value