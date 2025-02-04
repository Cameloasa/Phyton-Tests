from src.discussion import bigger_than_100, number_equal_with_42, calculate_length, is_true, compare_and_return, \
    sum_list


#1a
def test_bigger_than_100():
    expected = False
    actual = bigger_than_100(1)
    assert expected == actual

#1b
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

#1c
def test_length_less_than_5():
    text = "abc"
    expected = "Sorry, you must add 2 more characters to reach 5."  # 5 - 3 = 2
    actual = calculate_length(text)
    assert actual == expected

def test_length_equal_to_5():
    text = "abcde"
    expected = "This text has 5 characters, 0 more than 5."
    actual = calculate_length(text)
    assert actual == expected

def test_length_greater_than_5():
    text = "abcdefgh"
    expected = "This text has 8 characters, 3 more than 5."
    actual = calculate_length(text)
    assert  expected == actual

def test_length_empty_string():
    text = ""
    expected = "Sorry, you must add 5 more characters to reach 5." #5-0=5
    actual = calculate_length(text)
    assert actual == expected

def test_length_with_spaces():
    text = "  a b  "  # Length is 7 because spaces are counted
    expected = "This text has 7 characters, 2 more than 5." #7-5=2
    actual = calculate_length(text)
    assert actual == expected

def test_length_with_special_characters():
    text = "!@#$%^"  #Length is 6
    expected = "This text has 6 characters, 1 more than 5." #6-5=1
    actual = calculate_length(text)
    assert actual == expected

#1d
def test_is_true_with_true():
    assert is_true(True) == True

def test_is_true_with_false():
    assert is_true(False) == False

#1e
def test_less_than_5():
    assert compare_and_return(3) == [1, 2, 3]

def test_less_than_10():
    assert compare_and_return(7) == [5, 6, 7]

def test_less_than_15():
    assert compare_and_return(12) == [10, 11, 12]

def test_out_of_range():
    assert compare_and_return(15) == ["Out of range"]

def test_with_0():
    assert compare_and_return(0) == []

def test_with_1():
    assert compare_and_return(1) == [1]

def test_with_4():
    assert compare_and_return(4) == [1,2,3,4]

def test_with_9():
    assert compare_and_return(9) == [5, 6, 7, 8, 9]

def test_with_14():
    assert compare_and_return(14) == [10, 11, 12, 13, 14]

def test_with_negative():
    assert compare_and_return(-1) == []

def test_empty_list():
    expected = 0
    actual = sum_list([])
    assert expected == actual

def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([-1, 1, 0]) == 0
    assert sum_list([10, 20, 30]) == 60