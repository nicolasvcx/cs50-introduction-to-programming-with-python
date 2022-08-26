from numb3rs import validate

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("-1.0.0.1") == False
    assert validate("0.-1.0.0") == False
    assert validate("0.0.-1.0") == False
    assert validate("0.0.0.-1") == False

def test_letters():
    assert validate("cat.cat.cat.cat") == False

def test_letters():
    assert validate("1.0.0.1.1") == False



