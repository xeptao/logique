from fibonacci import fibonacci


def test_answer():
    # correctly calculates any input
    assert fibonacci(6) == 8

    # correctly calculates when n = 1 or n = 2
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
