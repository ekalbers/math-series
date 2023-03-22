from math_series import fibonacci, lucas, sum_series


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


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_ten():
    actual = lucas(10)
    expected = 2
    assert actual == expected


def test_lucas_twenty():
    actual = lucas(20)
    expected = 2
    assert actual == expected


def test_sum_series_ten():
    actual = sum_series(10)
    expected = 55
    assert actual == expected


def test_sum_series_ten_two_one():
    actual = sum_series(10, 2, 1)
    expected = 123
    assert actual == expected


def test_sum_series_ten_twenty_thirty():
    actual = sum_series(10, 20, 30)
    expected = 2330
    assert actual == expected
