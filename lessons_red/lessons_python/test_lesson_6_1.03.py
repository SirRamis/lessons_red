import pytest

def sum_it(x, y):
    return x + y

def test_equal():
    assert sum_it(5, 3) == 8



