# LOGICAL OPERATORS EXAMPLES
# -----------------------

doesOneEqualOne = (1 == 1) # 1 does equal one, so doesOneEqualOne evaluates to True

print("doesOneEqualOne: " + str(doesOneEqualOne))




doesOneNotEqualOne = (1 != 1) # 1 does equal one, so doesOneNotEqualOne evaluates to False

print("doesOneNotEqualOne: " + str(doesOneNotEqualOne))




doesWordEqualWord = ("Word" != "Word") # Word does equal Word so doesWordEqualWord evaluates to False

print("doesWordEqualWord: " + str(doesWordEqualWord))




isTwoGreaterThanOne = (2 > 1) # True

print("isTwoGreaterThanOne: " + str(isTwoGreaterThanOne))




isOneGreaterOrEqualToOne = (1 >= 1) # True

print("isOneGreaterOrEqualToOne: " + str(isOneGreaterOrEqualToOne))




isTwoLessOrEqualToOne = (2 <= 1) # False

print("isTwoLessOrEqualToOne: " + str(isTwoLessOrEqualToOne))




advancedLogicalStatementOne = (2 > 1) and (1 > 2) # one of these is false, so advancedLogicalStatementOne evluates to false

print("advancedLogicalStatementOne: " + str(advancedLogicalStatementOne))





advancedLogicalStatementTwo = (2 > 1) or (1 > 2) # one of these is true, so advancedLogicalStatementOne evluates to true

print("advancedLogicalStatementTwo: " + str(advancedLogicalStatementTwo))



# IF'S, AND SWITCHES EXAMPLES
# -----------------------

def isFace(inputWord):
    face = "face"
    notFace = "not face"

    if not inputWord == face: # if inputWord (a paramter) is not exactly "face", print notFace
        return "Sorry, that's " + notFace
    else:
        return "Yes, that's " + face # else, print face

isAFace= isFace("arm")

print(isAFace)




def divideIfGreaterThanAndLessThan(inputNumber):

    if inputNumber <= 10: # if inputNumber is less than or equal to 10
        quotient = inputNumber / 2
        print(f"divideIfGreaterThan: {inputNumber} divided by 2 equals {quotient}")
    elif (inputNumber < 20) and (inputNumber > 10): # elif is short for else if -> else if inputNumber is greater than 10 and less than 20 (10 < x < 20)
        product = inputNumber * 2
        print(f"divideIfGreaterThanAndLessThan: {inputNumber} multiplied by 2 equals {product}")
    elif (inputNumber == 777) or (inputNumber == 333): # else if inputNumber is equal to exactly 777 or 333
        print(f"Nice.")
    else:
        print("Math is hard") # if condition is not explicitly handled, print "Math is hard"

divideIfGreaterThanAndLessThan(7) # pass argument 7

divideIfGreaterThanAndLessThan(13) # pass argument 13

divideIfGreaterThanAndLessThan(69) # pass argument 69



# Ternary statement
number = 10
isOddOrEven = "Even" if number == 10 else "Odd" # This is a "ternary statement". It is a shorthanded way to evaluate variables to a boolean.
print("Ternary Statement: " + isOddOrEven)




def matchNumberToLetter(number):
    name = "matchNumberToLetter: "
    match number:    # this is traditionally called a switch statement but in python the syntax is "match"
        case 1:
            print(name + "A")
        case 2:
            print(name + "B")
        case 3:
            print(name + "C")
        case 4: 
            print(name + "D")
        case 5:
            print(name + "E")
        case _:        # _ is a way to handle incoming values that are not explicitly stated in the switch cases
            print(name + "unknown case")

matchNumberToLetter(4)

matchNumberToLetter(20)






