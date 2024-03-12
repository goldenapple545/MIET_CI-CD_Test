#!/usr/bin/python3

import pytest

def divide_two_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0

    return result

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (2, 2, 1),
    (6, 3, 2),
    (2, 0, 0)
])
def test_divide_two_numbers(a, b, expected):
    assert divide_two_numbers(a, b) == expected