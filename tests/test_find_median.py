
from src.find_median import find_median

"""
✔Funk ska returnera None om listan är tom.
✔Funk ska returnera elementet om listan har ett enda element.
✔Funk ska returnera det mittersta elementet om listan har ett udda antal element.
✔Funk ska returnera medelvärdet av de två mittersta elementen om listan har ett jämnt antal element.
✔Listan kan innehålla både negativa och positiva tal.
✔Listan behöver inte vara sorterad innan medianen beräknas.
"""

def test_find_median():
    assert find_median([]) is None
    assert find_median([7]) == 7
    assert find_median([3, 1, 2]) == 2
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([-5, -1, -3]) == -3
    assert find_median([10, 2, 38, 23, 38, 23, 21]) == 23
