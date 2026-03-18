from Calculator import Calculator

def main():
    print("--- Python CLI Calculator ---")
    print("Supported operators: +, -, *, /, **, >, <")
    print("Type 'exit' as the operator to quit.")

    # The keyword while = a "while loop"
    # This is an infinite loop because the condition True always equals true, this program will never exit unless specified
    # You can exit programs in the terminal using ctrl + c (cancel)
    while True:                                    
        try:                                                
            # Get user inputs
            num1_input = input("\nEnter first number: ")    # input() is a built in method that asks the user for a value in the terminal. 
                                                            # \n is a way for the terminal to start a new line
            operator = input("Enter operator: ").strip()    # strip is a method pulls withspace off strings -> https://www.w3schools.com/python/ref_string_strip.asp

            # Check if the user wants to quit
            if operator.lower() == 'exit':                  # Offer a way for the program to exit by allowing string value "exit" when asked for operator input in the terminal
                print("Goodbye!")
                break

            num2_input = input("Enter second number: ")

            # Convert inputs to floats (numbers)
            n1 = float(num1_input)   # built-in method similar to str()
            n2 = float(num2_input)   # built-in method similar to str()

            # Instantiate the class
            # We use the constructor
            my_calc = Calculator(n1, operator, n2)

            # Perform the calculation
            # This triggers the match statement that calls Calculator's methods
            my_calc.calculate()

        except ValueError:                                                      # ValueError is a built in type that the creators of python included for handling mismatched types
            print("Error: Please enter valid numeric values for the numbers.")  # More about ValueError -> https://www.w3schools.com/python/ref_exception_valueerror.asp
        except Exception as e:                                                  # Exception is also a built in type for handling generic errors
            print(f"An unexpected error occurred: {e}")                         # More about Exceptions -> https://www.w3schools.com/python/python_ref_exceptions.asp

if __name__ == "__main__":       # In Python, the line if __name__ == "__main__": acts as a gatekeeper.              
    main()                       # It determines whether the script is being run directly by you or being imported as a module into another script.      
                                 # To understand this, you need to know that Python automatically sets a special built-in variable called __name__ for every file.
                                 # When you run your calculator script directly (by typing python useCalcWithInput.py in your terminal), Python assigns the string "__main__" to the __name__ variable.
                                 # Try running this program by typing "python useCalcWithInput.py" (make sure you cd into "Dojo Session 4")
