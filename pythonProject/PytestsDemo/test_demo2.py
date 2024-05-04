import pytest


def test_file():
    greeting = "hello"
    assert greeting == "hi"


def test_sum():
    a=4
    b=6
    assert a+2==6

@pytest.mark.smoke
def test_Creditcardloan():
    debt=100
    interest=10
    print(debt+interest)
    assert (debt+interest)==110,"outstanding amount is correct"