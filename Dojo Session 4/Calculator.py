class Calculator:
    def __init__(self, num1, operator, num2):           # __init__ is a special keyword in python called a constructor
        self.num1 = num1                                # a constructor is a class specific mechanism for defining variables and values within a class
        self.operator = operator                        # constructors are responsible for defining what variables are included in the class
        self.num2 = num2                                # "self" is a conventional name for the first parameter referring to this class
        self.result = None                              # if you hover your mouse over __init__ and look at the params, self is a parameter that references this class
                                                        # result exists within the class but is not required to construct an object, it resides as a property

    def calculate(self):                                # Because calculate is a function within a class, it is now called a method
        match self.operator:
            case "+":
                self.add()                              # call to method within this class
            case "-":
                self.subtract()                         # call to method within this class
            case "*":
                self.multiply()                         # call to method within this class
            case "/":
                self.divide()                           # call to method within this class
            case "**":
                self.calculatePower()                   # call to method within this class
            case ">":
                self.isGreaterThan()                    # call to method within this class
            case "<":
                self.isLessThan()                       # call to method within this class
            case _:                                        
                self.result = "Error: Check yourself"

    # Methods for Basic Arithmetic

    def add(self):
        self.result = self.num1 + self.num2
        self.printResult()

    def subtract(self):
        self.result = self.num1 - self.num2
        self.printResult()        

    def multiply(self):
        self.result = self.num1 * self.num2
        self.printResult()

    def divide(self):
        if self.num2 != 0:                              # handle not being able to divide by 0
            self.result = self.num1 / self.num2
            self.printResult()
        else:
            self.result = "Error: Division by zero"
            self.printResult()

    def calculateGeneric(self):
        if self.operator == "+":
            self.result = self.num1 + self.num2
            self.printResult()

    def calculatePower(self):                           # Take self as a paramter - the class will automatically pass self when these methods are called
        if self.operator == "**":
            self.result = self.num1 ** self.num2
        else:
            self.result = "Error: check yourself"
            self.printResult()

    def isGreaterThan(self):                            # isGreaterThan is a "method" that is a "member" of the class "Calculator"
        self.result = self.num1 > self.num2             # Evaluating a True or False value here, not numbers. Result will equal True or False.
        self.printResult()

    def isLessThan(self):
        self.result = self.num1 < self.num2             # Evaluating a True or False value here, not numbers. Result will equal True or False.
        self.printResult()

    def printResult(self):
        print("printResult: " + str(self.result))

    def returnResult(self):                  
        return self.result