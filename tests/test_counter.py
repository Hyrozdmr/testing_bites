from lib.counter import*
def test_add():
    subject = Counter()
    subject.add(2)
    assert subject.count == 2
def  test_report():
    subject = Counter()
    result = f"Counted to {subject.count} so far."
    assert subject.count == 0