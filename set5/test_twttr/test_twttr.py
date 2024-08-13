from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("123") == "123"
    assert shorten('"') == '"'
    assert shorten("!?...") == "!?..."
