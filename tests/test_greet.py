from lib.greet import *

def test_greet_with_valid_input():
        result = greet("Amber")
        assert result == "Hello, Amber!"


def test_great_with_empty_input():    
        result = greet("")
        assert result == "Hello, !"


