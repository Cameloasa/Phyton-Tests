import pytest

from src.discussion import bigger_than_100, number_equal_with_42, calculate_length, is_true, compare_and_return, \
    sum_list, count_vowels, find_max, find_2nd_max, verify_number, find_2nd_max_version_2

#1a
"""
✔ Funktionen ska returnera True om x är större än 100.
✔ Funktionen ska returnera False om x är 100 eller mindre.
✔Funktionen ska fungera för både positiva och negativa heltal.
✔ Testfall ska verifiera att funktionen returnerar förväntade värden för olika ekvivalensklasser (t.ex. x < 100, x = 100, x > 100).
x < 100 (t.ex. x = 50, x = -10, x = 0)
x = 100 (gränsfall)
x > 100 (t.ex. x = 101, x = 200, x = 1000)
"""
def test_bigger_than_100():
    # x < 100 ska returnera False
    assert bigger_than_100(1) == False
    assert bigger_than_100(50) == False
    assert bigger_than_100(-10) == False
    assert bigger_than_100(0) == False

    # x = 100 ska returnera False
    assert bigger_than_100(100) == False

    # x > 100 ska returnera True
    assert bigger_than_100(101) == True
    assert bigger_than_100(200) == True
    assert bigger_than_100(1000) == True

"""
✔Om y < 42, ska funktionen returnera "Number y is less than '42'".
✔Om y > 42, ska funktionen returnera "Number y is more than '42'".
✔ Om y == 42, ska funktionen returnera "Number 42 is equal with '42'".
✔Funktionen ska fungera för negativa tal, positiva tal och 42.
✔Testfall ska verifiera att funktionen returnerar rätt värde för följande ekvivalensklasser:
y < 42 (t.ex. y = 41, y = 0, y = -10)
y = 42 (gränsfall)
y > 42 (t.ex. y = 43, y = 100, y = 1000)
"""
#1b
def test_number_equal_with_42():
    expected = "Number 42 is equal with '42'"
    actual = number_equal_with_42(42)  # Call the function!
    assert expected == actual

    expected_less = "Number 41 is less than '42'"
    actual_less = number_equal_with_42(41)
    assert expected_less == actual_less

    expected_more = "Number 43 is more than '42'"
    actual_more = number_equal_with_42(43)
    assert expected_more == actual_more

#Variant 2
@pytest.mark.parametrize("y, expected", [
    (42, "Number 42 is equal with '42'"),
    (41, "Number 41 is less than '42'"),
    (0, "Number 0 is less than '42'"),
    (-10, "Number -10 is less than '42'"),
    (43, "Number 43 is more than '42'"),
    (100, "Number 100 is more than '42'"),
    (1000, "Number 1000 is more than '42'")
])
def test_number_equal_with_42(y, expected):
    assert number_equal_with_42(y) == expected

"""
✔ Funktionen ska ta en sträng text som input och returnera ett meddelande baserat på dess längd.
✔ Om len(text) >= 5, ska funktionen returnera:

"This text has X characters, Y more than 5.", där X är textens längd och Y = len(text) - 5.
✔ Om len(text) < 5, ska funktionen returnera:
"Sorry, you must add Z more characters to reach 5.", där Z = 5 - len(text).
✔Funktionen ska korrekt hantera:
Strängar kortare än 5 tecken (text = "abc", text = "")
Strängar exakt 5 tecken (text = "abcde")
Strängar längre än 5 tecken (text = "abcdefgh")
Strängar med mellanslag (text = " a b ")
Strängar med specialtecken (text = "!@#$%^")
✔ Funktionen ska räkna alla tecken, inklusive mellanslag och specialtecken.
"""
#1c
def test_length_less_than_5():
    text = "abc"
    expected = "Sorry, you must add 2 more characters to reach 5."  # 5 - 3 = 2
    actual = calculate_length(text)
    assert actual == expected

def test_length_equal_to_5():
    text = "abcde"
    expected = "This text has 5 characters, 0 more than 5."
    actual = calculate_length(text)
    assert actual == expected

def test_length_greater_than_5():
    text = "abcdefgh"
    expected = "This text has 8 characters, 3 more than 5."
    actual = calculate_length(text)
    assert  expected == actual

def test_length_empty_string():
    text = ""
    expected = "Sorry, you must add 5 more characters to reach 5." #5-0=5
    actual = calculate_length(text)
    assert actual == expected

def test_length_with_spaces():
    text = "  a b  "  # Length is 7 because spaces are counted
    expected = "This text has 7 characters, 2 more than 5." #7-5=2
    actual = calculate_length(text)
    assert actual == expected

def test_length_with_special_characters():
    text = "!@#$%^"  #Length is 6
    expected = "This text has 6 characters, 1 more than 5." #6-5=1
    actual = calculate_length(text)
    assert actual == expected

"""
✔ Funktionen ska ta en boolesk variabel z som input.
✔Om z == True, ska funktionen returnera True.
✔ Om z == False, ska funktionen returnera False.
✔ Funktionen ska testas för följande ekvivalensklasser:

z = True → returnerar True
z = False → returnerar False
"""
#1d
def test_is_true_with_true():
    assert is_true(True) == True

def test_is_true_with_false():
    assert is_true(False) == False

def test_is_true_with_non_boolean_values():
    assert is_true(1) == True   # I Python är 1 sann
    assert is_true(0) == False  # 0 är falsk
    assert is_true(None) == False  # None är falsk
    assert is_true("Hello") == True  # En icke-tom sträng är sann
    assert is_true("") == False  # En tom sträng är falsk

#1f
"""
✔ Funktionen ska ta ett heltal w som input och returnera ett meddelande baserat på dess värde.
✔ Om w är 32, 64 eller 128, ska funktionen returnera "{w} is a valid number".
✔ Om w har något annat värde, ska funktionen returnera "This number is not valid".
✔ Funktionen ska testas för följande ekvivalensklasser:

Giltiga tal: w = 32, w = 64, w = 128
Ogiltiga tal: w = 31, w = 33, w = 63, w = 65, w = 127, w = 129
Specialfall: w = 0, w = -1, w = 999
"""

@pytest.mark.parametrize("w, expected", [
    (32, "32 is a valid number"),
    (64, "64 is a valid number"),
    (128, "128 is a valid number"),
    (31, "This number is not valid"),
    (33, "This number is not valid"),
    (63, "This number is not valid"),
    (65, "This number is not valid"),
    (127, "This number is not valid"),
    (129, "This number is not valid"),
    (0, "This number is not valid"),
    (-1, "This number is not valid"),
    (999, "This number is not valid")
])
def test_verify_number(w, expected):
    assert verify_number(w) == expected


#1g
"""
✔ Funktionen ska ta ett heltal x som input och returnera en lista baserat på följande regler:

Om x < 5, returnera en lista med tal från 1 till x.
Om 5 ≤ x < 10, returnera en lista med tal från 5 till x.
Om 10 ≤ x < 15, returnera en lista med tal från 10 till x.
Om x ≥ 15, returnera [].
✔ Funktionen ska testas för följande ekvivalensklasser:
x < 5: x = -1, x = 0, x = 1, x = 4
5 ≤ x < 10: x = 5, x = 9
10 ≤ x < 15: x = 10, x = 14
x ≥ 15: x = 15, x = 20, x = 100
"""
def test_less_than_5():
    assert compare_and_return(3) == [1, 2, 3]

def test_less_than_10():
    assert compare_and_return(7) == [5, 6, 7]

def test_less_than_15():
    assert compare_and_return(12) == [10, 11, 12]

def test_out_of_range():
    assert compare_and_return(15) == []

def test_with_0():
    assert compare_and_return(0) == []

def test_with_1():
    assert compare_and_return(1) == [1]

def test_with_4():
    assert compare_and_return(4) == [1,2,3,4]

def test_with_9():
    assert compare_and_return(9) == [5, 6, 7, 8, 9]

def test_with_14():
    assert compare_and_return(14) == [10, 11, 12, 13, 14]

def test_with_negative():
    assert compare_and_return(-1) == []

def test_empty_list():
    expected = 0
    actual = sum_list([])
    assert expected == actual
#Variant 2
@pytest.mark.parametrize("x, expected", [
    (-1, []),  # Negativt tal
    (0, []),   # x = 0 ska returnera en tom lista
    (1, [1]),
    (4, [1, 2, 3, 4]),
    (5, [5]),
    (9, [5, 6, 7, 8, 9]),
    (10, [10]),
    (14, [10, 11, 12, 13, 14]),
    (15, []),  # Out of range, returnerar en tom lista
    (20, []),
    (100, [])
])
def test_compare_and_return(x, expected):
    assert compare_and_return(x) == expected

"""
✔ Funktionen ska ta en lista av heltal som input och returnera summan av alla tal i listan.
✔ Om listan är tom, ska funktionen returnera 0.
✔ Funktionen ska fungera för alla typer av heltal: positiva, negativa och noll.
✔ Testfall ska inkludera följande ekvivalensklasser:

Lista med ett enda positivt tal
Lista med flera positiva tal
Lista med blandade positiva och negativa tal
Lista med nollor
Tom lista
"""
#2
def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([-1, 1, 0]) == 0
    assert sum_list([10, 20, 30]) == 60

# Testfall för en tom lista
def test_empty_list_sum_list():
    assert sum_list([]) == 0  # Tom lista ska ge 0

"""

"""
#3a
def test_no_vowels():
    expected = 0
    actual = count_vowels("qwrt")
    assert expected == actual

    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

def test_only_vowels():
    assert count_vowels("aeio") == 4
    assert count_vowels("ouyåäö") == 6
    assert count_vowels("öAE") == 3
    assert count_vowels("a") == 1

def test_mixed_letters():
    assert count_vowels("hello") == 2
    assert count_vowels("PyCharm") == 2
    assert count_vowels("automation") == 6

def test_case_insensitive():
    assert count_vowels("AeIoU") == 5
    assert count_vowels("PYTHON") == 2

"""
✔ Funktionen ska ta en lista av heltal som input.
✔ Om listan innehåller element ska den returnera det största talet.
✔ Om listan är tom ska funktionen returnera None.
✔ Testfall ska inkludera både positiva och negativa tal, samt tomma listor.
"""
#4
def test_find_max():
    # Testfall för vanliga fall
    assert find_max([1, 2, 3, 4, 5]) == 5  # Vanliga positiva tal
    assert find_max([10, 99, 32, 47]) == 99  # Blandade positiva tal
    assert find_max([-5, -2, -9, -1]) == -1  # Alla negativa tal
    assert find_max([42]) == 42  # Endast ett tal

    # Testfall för tom lista
    assert find_max([]) == None  # Tom lista

    # Testfall för specialfall
    assert find_max([5, 5, 5, 5]) == 5  # Alla lika tal
    assert find_max([0, 0, 0, 0]) == 0  # Alla nollor
    assert find_max([10, -20, 15, -5]) == 15  # Blandade positiva och negativa tal
    assert find_max([1000000, 10000001, 5000000, 20000000]) == 20000000  # Stora tal

"""
✔ Om listan innehåller två eller fler unika tal, ska den returnera det näst största talet.
✔ Om listan har exakt ett unikt tal, ska funktionen returnera det talet.
✔ Om listan har mindre än två element ska funktionen returnera None.
✔ Om alla tal är lika, ska funktionen returnera det enda talet (det finns inget "näst största").
"""
#5
def test_find_2nd_max():
    # Testfall för vanliga fall med olika tal
    assert find_2nd_max([1, 2, 3, 4, 5]) == 4  # Näst största tal i en lista
    assert find_2nd_max([10, 99, 32, 47]) == 47  # Blandade positiva tal
    assert find_2nd_max([-5, -2, -9, -1]) == -2  # Negativa tal

    # Testfall för specialfall
    assert find_2nd_max([7, 7, 7, 7]) == 7  # Alla tal lika
    assert find_2nd_max([42]) == None  # Endast ett tal
    assert find_2nd_max([]) == None  # Tom lista

    # Testfall för delad förstaplats
    assert find_2nd_max([5, 5]) == 5  # Delad förstaplats med två lika tal
    assert find_2nd_max([5, 5, 3, 3, 2]) == 3  # Delad förstaplats med flera lika tal

    # Testfall för blandade positiva och negativa tal
    assert find_2nd_max([-10, 15, 15, 20]) == 15  # Blandade negativa och positiva tal

    # Testfall för många olika tal
    assert find_2nd_max([100, -200, 300, 50, 25]) == 100  # Många unika tal

def test_find_2nd_max_version_2():
    testdata = [1,2,4,3]
    expected = 3
    actual = find_2nd_max_version_2(testdata)
    assert expected == actual

def test_find_2nd_max_version_2_returner_none():
    testdata = []
    expected = None
    actual = find_2nd_max_version_2(testdata)
    assert expected == actual