from src.example import add


def test_add_positive_numbers():
    expect = 5
    actual = add(2,3)
    assert expect == actual

def test_fail():
    assert True