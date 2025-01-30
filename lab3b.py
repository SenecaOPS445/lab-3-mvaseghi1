#!/usr/bin/env python3
'''Lab 3b Part 1 script - functions'''
# Author ID: [mvaseghi1]
# Author: Mohammad Vaseghi
# Author ID: 130349228
# Date Created: 2025/01/29
def sum_numbers(number1, number2):
    return int(number1 + number2)


def subtract_numbers(number1, number2):
    return int(number1 - number2)

def multiply_numbers(number1, number2):
    return int(number1 * number2)
if __name__ == '__main__': #When you import a script (import lab3b), Python loads it as a module but does not execute code inside 
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
    