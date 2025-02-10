
def add(x,y):
    return x + y

def subtract(x:int,y:int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("x, y  must be integers!")
    return x-y

def compare_names(input, name):
    if not isinstance(input, str):
        return False
    if not isinstance(name, str):
        return False
    name_small = name.casefold()
    input_small = input.casefold()
    position = name_small.casefold().find(input_small)
    if position == -1:
        return False
    else:
        return True

