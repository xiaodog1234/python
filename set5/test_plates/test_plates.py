from plates import is_valid

def test_is_valid():
    assert is_valid("A2") == False
    assert is_valid("HELLO") == True
    assert is_valid("hello") == True
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("123ABC") == False
    assert is_valid("ab.d") == False
    assert is_valid("AB123A") == False
