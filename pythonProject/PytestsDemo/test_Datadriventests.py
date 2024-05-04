import pytest

from PytestsDemo.baseclass import BaseClass
from PytestsDemo.conftest import testdataload


@pytest.mark.usefixtures("setup","testdataload")
class TestCheck(BaseClass):
    def test_1(self, testdataload):
        log=self.getlogger()
        print("Iam Test 1")
        log.info(testdataload[0])
        # print(testdataload[0])

    def test_2(self, testdataload):
        print("Iam Test 2")
        log = self.getlogger()
        log.info(testdataload[1])
        # print(testdataload[1])

    def test_3(self, testdataload):
        print("Iam Test 3")
        log = self.getlogger()
        log.info(testdataload[2])
        # print(testdataload[2])
