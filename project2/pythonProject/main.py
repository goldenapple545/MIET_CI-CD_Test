#!/usr/bin/python3

def divide_two_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0

    return result