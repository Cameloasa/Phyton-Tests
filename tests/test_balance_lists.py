"""
✔ Accepteras två listor av vilken längd som helst.
✔Element kan flyttas mellan listorna för att balansera dem.
✔Till slut ska skillnaden i längd mellan de två listorna vara högst 1.
✔ Ordningen på elementen spelar ingen roll.
✔Den ursprungligen längre listan måste överföra sina element till den andra listan.
✔Om listorna redan är balanserade, behöver ingen förändring göras.
"""
from src.balance_lists import balance_lists


def test_balanced_list_remain_unchanged():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    balance_lists(list1,list2)
    assert len(list1) == 3
    assert len(list2) == 3

def test_edge_case_empty_list():
    list1 = []
    list2 = [1, 2, 3, 4]
    balance_lists(list1, list2)
    assert abs(len(list1) - len(list2)) <= 1
