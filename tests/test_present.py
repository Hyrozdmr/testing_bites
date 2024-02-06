import pytest
from lib.present import *
def test_wraping_already_wrapped():
    subject = Present()
    subject.wrap(29)
    with pytest.raises(Exception) as err:
        subject.wrap(55)
    error_mesage = str(err.value)
    assert error_mesage == "A contents has already been wrapped."

def test_unwrapped_witout_wrapping():
    subject = Present()
    with pytest.raises(Exception) as err:
        subject.unwrap()
    error_mesage = str(err.value)
    assert error_mesage == "No contents have been wrapped."

