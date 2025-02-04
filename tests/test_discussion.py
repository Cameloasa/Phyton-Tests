from src.discussion import bigger_than_100


def test_bigger_than_100():
    expected = False
    actual = bigger_than_100(1)
    assert expected == actual