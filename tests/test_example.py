from src.example import add, compare_names


def test_add_positive_numbers():
    expect = 5
    actual = add(2,3)
    assert expect == actual

def test_fail():
    assert True

def test_compareNames__input_is_not_a_string():
    expect = False
    actual = compare_names(123,"Name")
    assert expect == actual


def test_compareNames__input_is_not_a_string():
    expect = False
    actual = compare_names("kal",123)
    assert expect == actual

def test_compareNames__input_is_in_name():
    expect = True
    actual = compare_names("kal","Kalle")
    assert expect == actual

#TODO expected false om namnen inte matchar