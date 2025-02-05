
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

print(compare_and_return(3))
print(compare_and_return(7))
print(compare_and_return(12))
print(compare_and_return(15))
print(compare_and_return(0))
print(compare_and_return(1))
print(compare_and_return(4))
print(compare_and_return(9))
print(compare_and_return(14))
print(compare_and_return(15))
print(compare_and_return(-1))

#2 Det har smugit sig in kommentarer i stället för kod på några ställen.
# Skriv färdigt testfallen test_empty_list och test_number_list.
# Returnerar summan av alla tal i listan
def sum_list(numbers: list) -> int:
    return sum(numbers)

#3a Diskutera följande kod.
# Räcker det med ett testfall för att testa funktionen?
def count_vowels(word: str) -> int:
    vowels = "aeiouyåäöAEIOUYÅÄÖ"
    return sum(1 for char in word if char in vowels)

#4 Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

#5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
def find_2nd_max(numbers):
    if len(numbers) < 2:
        return None

    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    if len(unique_numbers) < 2:
        return unique_numbers[0]

    return unique_numbers[1]


