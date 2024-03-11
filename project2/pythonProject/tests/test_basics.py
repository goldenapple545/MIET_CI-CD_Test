#!/usr/bin/python3

import pytest
from main import divide_two_numbers

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (2, 2, 1),
    (6, 3, 2),
    (2, 0, 0)
])
def test_divide_two_numbers(a, b, expected):
    assert divide_two_numbers(a, b) == expected