from src.is_sorted_ascending import is_sorted_ascending

"""
✔Om listan är tom, måste den returnera True.
✔Om listan har ett enda element, måste den returnera True.
✔Om listan är sorterad i stigande ordning, måste den returnera True.
✔Om listan inte är sorterad, måste den returnera False.
"""
def test_is_sorted_ascending():
    assert is_sorted_ascending([]) == True          # ✅ listan är tom
    assert is_sorted_ascending([5]) == True         # ✅ listan har ett enda element
    assert is_sorted_ascending([1, 2, 3, 4]) == True  # ✅ listan är sorterad i stigande ordning
    assert is_sorted_ascending([3, 1, 2]) == False   # ❌ listan är inte sorterad i stigande ordning
    assert is_sorted_ascending([2, 2, 2]) == True   # ✅ samma element i listan
    assert is_sorted_ascending([5, 4, 3, 2, 1]) == False  # ❌ listan är sorterad i stigande ordning
    assert is_sorted_ascending([-3, -2, -1, 0, 1]) == True