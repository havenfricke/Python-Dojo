from exports import add, subtract, multiply, divide, calculate # import specific functions from exports.py
from exports import * # import everything from exports.py

# When you use keywords "from" and "import", python will automatically add a folder called __pychache__ in your project
# This file tells the python interpreter that there are components of a program being imported   

print(add(2, 2)) # If a function can handle more than two arguments but less are passed, they must be given a value where params are specified

print(add(2, 2, 4, 2)) # If you hover your mouse over the add() function, it will tell you the parameters / arguments expected

print(subtract(10, 5)) # The data type expected to be returned is also mentioned if you hover over the function
                       # In this case a string is expected to be returned

print(subtract(10, 2, 2, 2)) # By holding crtl and clicking a function, you can "follow" where the function is located with VS Code
                             # If a function is not imported properly, the "follow" macro does not work
                             # You can use this to determine if something has been properly or improperly imported
print(multiply(100, 2))

print(divide(100, 2))

print(calculate(2, "+", 2)) # When parameters are specified in a function declaration, arguments need to be passed in the expected order

print(calculate(10, "-", 5))

print(calculate(100, "*", 2))

print(calculate(100, "/", 2))

print(calculate(10, "divide", 2))

print(calculate(100, "multiply", 5))

print(calculate("test", "for", "default handling")) # Expect default in switch statement, "Error: Check yourself"
