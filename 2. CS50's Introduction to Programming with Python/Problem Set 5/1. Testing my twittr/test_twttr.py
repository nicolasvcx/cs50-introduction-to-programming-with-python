from twttr import shorten

def main():
    test_lower_case()
    test_upper_case()
    test_number()
    test_punctuation()

def test_lower_case():
    assert shorten("twitter") == "twttr"

def test_upper_case():
    assert shorten("TWITTER") == "TWTTR"

def test_number():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("?") == "?"

if __name__ == "__main__":
    main()