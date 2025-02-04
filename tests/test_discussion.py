from src.discussion import bigger_than_100, number_equal_with_42


def test_bigger_than_100():
    expected = False
    actual = bigger_than_100(1)
    assert expected == actual

def test_number_equal_with_42():
    expected = "Number 42 is equal with '42'"
    actual = number_equal_with_42(42)  # Call the function!
    assert expected == actual

    expected_less = "Number 41 is less than '42'"
    actual_less = number_equal_with_42(41)
    assert expected_less == actual_less

    expected_more = "Number 43 is more than '42'"
    actual_more = number_equal_with_42(43)
    assert expected_more == actual_more


