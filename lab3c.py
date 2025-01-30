#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: [mvaseghi1]
# Author: Mohammad Vaseghi
# Author ID: 130349228
# Date Created: 2025/01/29
# This script defines a function that performs basic arithmetic operations
# including addition, subtraction, and multiplication.

def operate(number1, number2, operator): 
    if operator == 'add': # If an unsupported operator is provided, an error message is returned.
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"' ## Return an error message if the operator is invalid
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide')) ## Will return Error: function operator can be "add", "subtract", or "multiply"


