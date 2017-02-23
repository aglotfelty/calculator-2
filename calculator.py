"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic2 import *

while True: 
    user_calculation = raw_input("> ")
    calculation_list = user_calculation.split(" ")
    if calculation_list[0] == "+":
        addition = add(int(calculation_list[1]), int(calculation_list[2])) 
        print addition
    elif calculation_list[0] == 'q':
        break

     
