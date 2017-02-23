"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *

while True: 
    user_calculation = raw_input("> ")
    calculation_list = user_calculation.split(" ")
    operator = calculation_list[0]
    list_length = len(calculation_list)
    if list_length == 3:
        try:
            num1 = int(calculation_list[1])
            num2 = int(calculation_list[2]) 
        except IndexError:
            if operator == "q":
                break
            else:
                print "I don't understand."
                continue
        if operator == "+":
            addition = add(num1, num2) 
            print addition
        elif operator == "-":
            subtraction = subtract(num1, num2)
            print subtraction
        elif operator == "*":
            multiplication = multiply(num1, num2)
            print multiplication
        elif operator == "/":
            division = divide(num1, num2)
            print division
        elif operator == "pow":
            raised_to_the_power = power(num1, num2)
            print raised_to_the_power
    else:
        try:
            num1 = int(calculation_list[1])
        except IndexError:
            if operator == "q":
                break
            else:
                print "I don't understand."
                continue
        if operator == "square":
            squared = square(num1)
            print squared
        elif operator == "cube":
            cubed = cube(num1)
            print cubed 




     
