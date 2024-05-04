def test_creditcardreq(setup):
    age=19
    if age>18:
        print("issue a creditcard")
        assert age>18,"creditcard issued"