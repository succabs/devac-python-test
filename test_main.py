import pytest


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def power(x, y):
    """Calculate x raised to the power y without using math.pow."""
    result = 1
    for _ in range(int(y)):
        result *= x
    return result


print(add(5, 4))  # --> 9
print(multiply(3, 4))  # --> 12
print(power(2, 8))  # --> 256


# Tests for add function
def test_add():
    assert add(6, 5) == 11
    assert add(0, 0) == 0
    assert add(-1, -9) == -10
    assert add(0, 2) != 3
    assert add(10, -5) != 10


# Tests for multiply function
def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(0, -10) == 0
    assert multiply(-20, 3) == -60
    assert multiply(0, 2) != 3
    assert multiply(5, 5) != 20


# Tests for power function
def test_power():
    assert power(2, 2) == 4
    assert power(10, 0) == 1
    assert power(60, 1) == 60
    assert power(4, 2) == 16
    assert power(5, 2) != 20
    assert power(2, 4) != 12
