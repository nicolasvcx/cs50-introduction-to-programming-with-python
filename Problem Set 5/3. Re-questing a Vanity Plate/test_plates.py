from plates import is_valid

def test_punctuaton():
    assert is_valid("AA!") == False

def test_beginning_characters():
    assert is_valid("04AA") == False
    assert is_valid("AB04") == False
    assert is_valid("A20") == False

def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTTIME") == False

def test_number_placement():
    assert is_valid("AA02B") == False
    assert is_valid("CS50P") == False