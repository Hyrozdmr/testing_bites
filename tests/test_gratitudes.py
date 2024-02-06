from lib.gratitudes import *

def test_add_gratitude_to_list():
    subject = Gratitudes()
    subject.add("Sun")
    subject.add("Health")
    result = subject.format()
    assert result == "Be grateful for: Sun, Health"


    