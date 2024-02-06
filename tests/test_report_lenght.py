from lib.report_length import*
def test_report_length():
    string = " "
    result =  report_length(string)
    assert result == f"This string was {len(string)} characters long."


