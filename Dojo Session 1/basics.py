# VARIABLES AND DATA TYPES EXAMPLES
# -----------------------

# string
a = 'python is dope'
# char
b = 'b'
# int
c = 1
# bool - I will go over more boolean stuff later (not in this script)
d = True
e = False
f = 1 # this integer is truthy
g = 0 # this integer is falsy
# float
h = 3.14
# double
i = 3.14159265359


# FUNCTION EXAMPLES
# ------------------------


# Declaration of a function (string concatenation)
def concatenateString():
    concatenatedString = "[Concat String]: " + a + " " + b
    print(concatenatedString) # print is python's way of sending data to the terminal / command line interface

# Function call - a function needs to be called within a program in order for it to run (should come after a declaration from top to bottom)
concatenateString()




# Declaration of a function with parameters / arguments
def concatStringWithParams(param1, param2):
    concatStringWithParams = "[Concat String w Params]: " + param1 + " " + param2
    print(concatStringWithParams)

# When you call a function and pass variables, they are called arguments instead of parameters
concatStringWithParams(a, b)




# Declaration of a function that returns values
# The keyword return does multiple things 1) outputs a value and 2) stops the code execution at return
def concatStringAndReturn():
    concatReturnString = "[Concat return string]: " + a + " " + b
    return concatReturnString # This function can now be treated like a variable
    # any code past a return statement is considered "unreachable code"

print(concatStringAndReturn())




# Declaration of a function with parameters that returns a string
def concatReturnStringWithParams(param1, param2):
    concatReturnString = "[Concat return string w params]: " + param1 + " " + param2
    return concatReturnString

storedString = concatReturnStringWithParams(a, b)
print(storedString)

# OR 

print(concatReturnStringWithParams(a, b))



# ARITHMETIC OPERATORS EXAMPLES
# --------------------------
# str() is a "built-in method". All computer languages come with tools you can use to manipulate data.
# We'll use str() to convert an integer to a string.
# more about that here -> https://docs.python.org/3/library/functions.html

def add():
    sum = f + g # 1 + 0 = 1
    stringSum = str(sum) # this converts numerical values to a string
    printString = "[Add]: " + stringSum
    print(printString)

add()



def subtract():
    difference = g - f # 0 - 1 = -1
    stringDiff = str(difference) # convert from int to string
    printString = "[Subtract]: " + stringDiff
    print(printString)

subtract()



def multiply():
    product = 2 * 4 # 2 * 4 = 8
    stringProd = f"[Multiply]: {product}" # This is called "string interpolation", another way to convert values to a string directly
    print(stringProd)

multiply()



def divide():
    quotient =  4 / 2 # 4 / 2 = 2 
    stringQuot = f"[Divide]: {quotient}" # Interpolate
    print(stringQuot)

divide()



def modulo():
    remainder = 4 % 3 # 4 / 3 leaves a remainder of 1 that goes undivided.
    print("[Modulo]: " + str(remainder))

modulo()



def powerOf(base, exponent):
    result = base ** exponent # 2 squared = 4
    return "[PowerOf]: " + str(result)

print(powerOf(2, 2))



def plusEquals():
    number = 5
    number += 2 # Number was declared at 5, += 2, it now equals 7
    print("[PlusEquals]: " + str(number))

plusEquals()



def minusEquals():
    number = 5
    number -= 2 # Number was declared at 5, -= 2, now equals 3
    print(f"[MinusEquals]: {number}")

minusEquals()



def multThenDivEquals():
    number = 5 
    number *= 2 # Number was declared at 5, *= 2, now equals 10
    number /= 2 # Number was declared at 5, /= 2, now equals 5
    print(f"[multThenDivEquals]: {number}")

multThenDivEquals()






































