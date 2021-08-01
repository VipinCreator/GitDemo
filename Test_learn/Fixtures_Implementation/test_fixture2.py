import pytest


@pytest.mark.usefixture("dataload")
class TestExample2:

    def test_profile(self,dataload):
        print(dataload)
