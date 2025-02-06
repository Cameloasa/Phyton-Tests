
"""
✔Funktionen ska returnera en lista med resultaten av multiplikationen
✔Om limit == 0, ska den returnera en tom lista ([]).
✔n måste vara ett positivt heltal (eller 0).
✔limit måste vara ett positivt heltal (eller 0).
✔Funktionen ska fungera för alla giltiga heltal.
"""
import pytest
from src.multiplication_table import multiplication_table


def test_multiplication_table():
    expected = [3, 6, 9, 12]
    actual = multiplication_table(3,4)
    assert expected == actual

def test_multiplication_table_limit_0():
    assert multiplication_table(5,0) == []

def test_multiplication_table_n_0():
    assert multiplication_table(0,3) == [0,0,0,]

def test_multiplication_table_limit_negativ():
    with pytest.raises(ValueError):
        multiplication_table(3, -1)


