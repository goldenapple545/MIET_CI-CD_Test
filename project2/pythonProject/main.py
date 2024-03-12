#!/usr/bin/python3

def divide_two_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0

    return result


print(divide_two_numbers(5, 2))
print("Real Hello World!!")
