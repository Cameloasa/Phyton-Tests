
#1 Vilka ekvivalensklasser har uttrycken?

#1a. x > 100
print("Uppgift 1-a------------")
def bigger_than_100(x: int) -> bool: #type hints
   return x > 100

print(bigger_than_100(1))
print(bigger_than_100(100))
print(bigger_than_100(101))

#1b. y == 42
print("Uppgift 1-b------------")
def number_equal_with_42(y: int) -> str:
    if y < 42:
        return f"Number {y} is less than '42'"
    elif y > 42:
        return f"Number {y} is more than '42'"
    else:
        return f"Number {y} is equal with '42'"

print(number_equal_with_42(41))
print(number_equal_with_42(42))
print(number_equal_with_42(43))

#1c. len(text) >= 5
print("Uppgift 1-c------------")
def calculate_length(text: str) -> str:
    length = len(text)
    if len(text) >= 5:
        return f"This text has {length} characters, {length - 5} more than 5."

    else:
        return f"Sorry, you must add {5 - length} more characters to reach 5."

print(calculate_length("mena"))
print(calculate_length("mening"))
print(calculate_length("meningar"))

#1d. z == True
print("Uppgift 1-d------------")
def is_true(z: bool) -> bool:
    return z is True

print(is_true(False))

#1e. 8 < v < 16 (9-15)
print("Uppgift 1-e------------")
def get_values_in_range(start: int, end: int) -> list[int]:
    if start >= end:
        return []
    return list(range(start + 1, end))

print(get_values_in_range(8,16))

#1f. w == 32 or w == 64 or w == 128
print("Uppgift 1-f------------")
def verify_number(w: int) -> str:
    if w in {32, 64, 128}:
        return f"{w} is a valid number"
    return "This number is not valid"

print(verify_number(32))
print(verify_number(31))
print(verify_number(64))
print(verify_number(63))
print(verify_number(128))
print(verify_number(130))

#1g. if x < 5: … elif x < 10: … elif x < 15: … else
print("Uppgift 1-g------------")
def compare_and_return(x: int) -> list[int]:
    if x < 5:
        return list(range(1, x + 1))
    elif x < 10:
        return list(range(5, x + 1))
    elif x < 15:
        return list(range(10, x + 1))
    return ["Out of range"]

print(compare_and_return(4))
print(compare_and_return(11))
print(compare_and_return(14))
print(compare_and_return(16))
