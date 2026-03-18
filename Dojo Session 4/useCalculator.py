from Calculator import Calculator as calc       # You can alias imports to names you want them to be, Calulator class can be referenced as calc 

# To get 100:
calc1 = calc(10, "**", 2)                       # Here you're using your class to "contruct" data
calc1.calculatePower()                          # Call the specific method

# To use the general calculate method:
calc2 = calc(10, "+", 5)                        # Here you're using your class to "contruct" data
calc2.calculate()

calc3 = calc(20, "/", 2)
calc3.calculate()


print(calc1, calc2, calc3)                      # This is going to print memory addresses in the format of 0xXXXXXX
                                                # In compsci, this is how any data is stored. At a memory address. 
                                                # Each time you are creating a variable and using it, you are pointing to a memory address to get a value.
                                                # Think of these addresses as street address like places we live as humans but instead for data objects in the digital realm

print(calc1.result, calc2.result, calc3.result) # This accesses the value at the address printed in the previous line of code
                                                # A memory address is like the street you live on and the value is like the apartment number or home number you live at
