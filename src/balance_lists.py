def balance_lists(list1:list,list2:list) -> tuple[list,list]:
    if len(list2) > len(list1):
        list1, list2 = list2, list1
    while len(list1) - len(list2) > 1:
        list2.append(list1.pop())