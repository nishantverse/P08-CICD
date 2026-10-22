from fine import calculate_fine

def test_no_fine_within_due_date():
    assert calculate_fine(0) == 0

def test_fine_for_late_return():
    assert calculate_fine(5) == 25

def test_negative_days():
    assert calculate_fine(-2) == 0
