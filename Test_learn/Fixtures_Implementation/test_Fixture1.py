import pytest

@pytest.mark.usefixtures("setup")


class TestFixture:

    def test_fixture1(self):
        print("I am test 1")

    def test_fixture3(self):
        print("I am part of same fixture1 file")
