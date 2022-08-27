from fuel import convert,gauge
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/5") == 20

def test_exception():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("A/B")