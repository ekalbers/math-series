from math_series import fibonacci


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_fibonacci_twenty():
    actual = fibonacci(20)
    expected = 6765
    assert actual == expected
