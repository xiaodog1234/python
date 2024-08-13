from bank import value


def test_value_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, Newman") == 0

def test_value_20():
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("HEY") == 20
    assert value("How you doing?") == 20

def test_value_100():
    assert value("What's happening") == 100
    assert value("What's up") == 100
    assert value("124") == 100
    assert value("-124") == 100
    assert value("") == 100
    #assert value(" hello ") == 100
    #assert value('"') == 100
