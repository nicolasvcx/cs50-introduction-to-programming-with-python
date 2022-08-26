from bank import value

def main():
    test_case_sensitivity()
    test_return_0()
    test_return_20()
    test_return_100()

def test_case_sensitivity():
    assert value("HeLlO") == 0
    assert value("HoW it'S GoInG?") == 20

def test_return_0():
    assert value("hello") == 0

def test_return_20():
    assert value("How you doing?") == 20

def test_return_100():
    assert value("Not H") == 100

if __name__ == "__main_":
    main()