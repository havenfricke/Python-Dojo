# The S in SOLID - Single-responsibility in context of this python program (exports.py)
# This python program or module is responsible for doing math
# Only functions that perform math should be allowed here
# Not all programmers do things like this but you will set yourself apart from a lot of sloppy devs by doing so
# Remember, only the cream rises to the top

# ------------------------------------------------------------------------------------

# if a function can handle more than two parameters but less are passed, they must be given a value. 
# Parameters num3 and num4 will default to 0 if no arguments are passed to this function in place of them.
# num1 and num2 are required for the function to run.

def add(num1, num2, num3 = 0, num4 = 0):
    return "Add:" + str(num1 + num2 + num3 + num4)


def subtract(num1, num2, num3 = 0, num4 = 0):
    return "Subtract: " + str(num1 - num2 - num3 - num4)


def multiply(num1, num2):
    return "Multiply: " + str(num1 * num2)


def divide(num1, num2):
    return "Divide: " + str(num1 / num2)


def calculate(num1, operator, num2):
    match operator:
        case "+":
            return "Calc: " + str(num1 + num2)
        case "add":
            return "Calc: " + str(num1 + num2)
        case "-":
            return "Calc: " + str(num1 - num2)
        case "subtract":
            return "Calc: " + str(num1 - num2)
        case "*":
            return "Calc: " + str(num1 * num2)
        case "multiply":
            return "Calc: " + str(num1 * num2)
        case "/":
            return "Calc: " + str(num1 / num2)
        case "divide":
            return "Calc: " + str(num1 / num2)
        case _:
            return "Error: Check yourself" # The default case when receiving values that are not specified
