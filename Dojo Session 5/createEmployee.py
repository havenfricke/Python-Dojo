from Employee import Employee    # (from FileName import ClassName)

employee = Employee(
    name="Haven Fricke",
    age=31,
    email="hfricke@bizness.com",
    phoneNumber="555-555-5555",
    role="Developer", 
    employee_id="EMP-1005", 
    salary=70000
    )

print(employee.name)        # Prints the name of the employee to the terminal

print(employee.employee_id) # Prints the employee_id to the terminal

print(employee)             # Prints and employee object and a memory address where the employee object is located to the terminal