from lib.count_words import *

def test_given_string():
    result = count_words("black, navy, red, yellow")
    assert result == 4
