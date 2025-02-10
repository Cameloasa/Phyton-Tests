import pytest

from src.example import (add,
                         compare_names,
                         subtract)


def test_add_positive_numbers():
    expect = 5
    actual = add(2,3)
    assert expect == actual

def test_fail():
    assert True

def test_subtract_positive_number():
    expect = 2
    actual = subtract(5,3)
    assert expect == actual

def test_subtract_not_integers():
    with pytest.raises(TypeError):
        subtract(5,"3")

def test_compare_names__input_is_not_a_string():
    expect = False
    actual = compare_names(123,"Name")
    assert expect == actual


def test_compare_names_name_is_not_a_string():
    expect = False
    actual = compare_names("kal",123)
    assert expect == actual

def test_compare_names__input_is_in_name():
    expect = True
    actual = compare_names("kal","Kalle")
    assert expect == actual

#
def test_compare_names__input_not_matches():
    expect = False
    actual = compare_names("kal", "mal")
    assert expect == actual