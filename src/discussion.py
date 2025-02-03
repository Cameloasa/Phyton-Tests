
#1 Vilka ekvivalensklasser har uttrycken?

#1a. x > 100
def bigger_than_100(x):
    if x <= 100:
        return False
    else:
        return True

print(bigger_than_100(1))
print(bigger_than_100(100))
print(bigger_than_100(101))

#1b. y == 42
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
#1e. 8 < v < 16
#1f. w == 32 or w == 64 or w == 128
#1g. if x < 5: … elif x < 10: … elif x < 15: … else
