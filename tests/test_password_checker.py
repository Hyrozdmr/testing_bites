import pytest
from lib.password_checker import *
def test_check_size_of_password():
    subject = PasswordChecker()
    subject.check("123abc45") == True
    subject.check("oasjdais!@@£") == True
    assert subject.check
    
    subject = PasswordChecker()
    with pytest.raises(Exception) as err:
        subject.check("asdsad")
    error_mesage = str(err.value)
    assert error_mesage == "Invalid password, must be 8+ characters."
    
