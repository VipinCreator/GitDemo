import pytest


def test_program():
    print("Hello")


@pytest.mark.smoke
def test_credit():
    print("Money credited")
