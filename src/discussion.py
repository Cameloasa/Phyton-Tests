
#1 Vilka ekvivalensklasser har uttrycken?

#1a. x > 100
print("Uppgift 1-a------------")
def bigger_than_100(x):
    if x <= 100:
        return False
    else:
        return True

print(bigger_than_100(1))
print(bigger_than_100(100))
print(bigger_than_100(101))

#1b. y == 42
print("Uppgift 1-b------------")
def number_equal_with_42(y):
    if y < 42:
        return print(f"Number {y} is less than '42'")
    elif y > 42:
        return print(f"Number {y} is more than '42'")
    else:
        return print(f"Number {y} is equal with '42'")

number_equal_with_42(41)
number_equal_with_42(42)
number_equal_with_42(43)

#1c. len(text) >= 5
print("Uppgift 1-c------------")
def calculate_length(text):
    if len(text) >= 5:
        more_chars = len(text) - 5
        print(f"This text has {len(text)} characters and you have {more_chars} chars than 5.")
    else:
        needed_chars = 5 - len(text)
        print(f"Sorry, you must add {needed_chars} more characters to reach 5.")

calculate_length("mena")
calculate_length("mening")
calculate_length("meningar")

#1d. z == True
print("Uppgift 1-d------------")
def char_vs_text(text):
    if len(text) == 1:
        return True
    else:
        return False

print(char_vs_text(""))
print(char_vs_text("a"))
print(char_vs_text("abc"))

#1e. 8 < v < 16 (9-15)
print("Uppgift 1-e------------")
def print_value_interval(start, end):
    if start >= end:
        print("Invalid interval. The first value must be more than end value")
    for value in range(start+1, end):
        print(value)

print_value_interval(8,16)
#1f. w == 32 or w == 64 or w == 128
print("Uppgift 1-f------------")
def verify_and_print(w):
    if w == 32:
        print(f"{w} is equal with 32")
    elif w == 64:
        print(f"{w} is equal with 64")
    elif w == 128:
        print(f"{w} is equal with 128")
    else:
        print("This number is not equal with 32, 64, or 128")

verify_and_print(32)
verify_and_print(33)
verify_and_print(64)
verify_and_print(65)
verify_and_print(128)
verify_and_print(130)

#1g. if x < 5: … elif x < 10: … elif x < 15: … else
def compare_and_print(x):
    if x < 5:
        for value in range(1, x + 1):
            print(value)
    elif x < 10:
        for value in range(5, x + 1):
            print(value)
    elif x < 15:
        for value in range(10, x + 1):
            print(value)
    else:
        print("Out of range")

compare_and_print(3)
compare_and_print(7)
compare_and_print(12)
compare_and_print(16)
