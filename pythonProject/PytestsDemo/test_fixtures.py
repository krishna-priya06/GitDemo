import pytest

def test_method(setup):
    print("I will be executing once fixture code is executed")

@pytest.fixture().
def setup():
    print("I will be executing first")
    yield
    print("I am a post test condition and I will be executing after test code is executed")


