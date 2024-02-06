from lib.string_builder import *

def test_initially_output_is_an_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_adding_a_strig():
    string_builder = StringBuilder()
    string_builder.add("hello world")
    assert string_builder.output() == "hello world"
    
def test_adding_a_strig_size():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.size() == 5