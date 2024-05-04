#test
#test
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    print("hello")

@pytest.mark.xfail
@pytest.mark.smoke
def test_secondprogram():
    print("Good Evening")

@pytest.mark.smoke
def test_creditcardreq():
    age=19
    if age>18:
        print("issue a creditcard")
        assert age>18,"creditcard issued"
