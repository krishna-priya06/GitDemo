import pytest


@pytest.mark.usefixtures("setup")
class TestCheck:
    def test_1(self):
        print("Iam Test 1")

    def test_2(self):
        print("Iam Test 2")

    def test_3(self):
        print("Iam Test 3")

