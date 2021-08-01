import pytest


@pytest.fixture(scope="class")
def setup():
    print("Hi I will execute first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataload():
    print("user data sent")
    return ["Vipin","vipin.pillai"]