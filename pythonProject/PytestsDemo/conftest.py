import pytest


@pytest.fixture(scope ="class")
def setup():
    print("I will be executing first")
    yield
    print("I am a post test condition and I will be executing after test code is executed")

@pytest.fixture()
def testdataload():
    return ['apple','orange','banana']
@pytest.fixture(params=[("chrome","kiran"),("Firefox","priya"),("IE","hira"),("safari","nakshatra")])
def crossbrowser(request):
    return request.param
