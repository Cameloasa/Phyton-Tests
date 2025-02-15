from src.autocomplete_list import autocomplete_list
from src.celsius_to_fahrenheit import c_to_f
from src.count_words import count_words
from src.find_median import find_median
from src.is_sorted_ascending import is_sorted_ascending
from src.multiplication_table import multiplication_table

print("1 - Omvandla Celsius(°C) till Fahrenheit(°F) c_to_f()")
print(f"-273.15°C == {c_to_f(-273.15)}°F")
print(f"-274°C == {c_to_f(-274)}°F")
print(f"-40°C == {c_to_f(-40)}°F")
print(f"100°C == {c_to_f(100)}°F")

print("2 - Returnerar antalet ord count_words()")
print("Antalet ord i('') ==" , count_words(""))
print("Antalet ord i(' ') ==" , count_words(" "))
print("Antalet ord i('hello') ==" , count_words("hello"))
print("Antalet ord i('hello world') ==" , count_words("hello world"))
print("Antalet ord i('  hello  world  ') ==" , count_words("  hello  world  "))
print("Antalet ord i('  hello  world    ! !') ==" , count_words("  hello  world    ! !"))

print("3 - Returnerar medianen från en lista med tal find_median().")
print(f"{find_median([])} == None")
print(f"{find_median([7])} == [7]")
print(f"{find_median([3, 1, 2])} == [3, 1, 2]")
print(f"{find_median([1, 2, 3, 4])} == [1, 2, 3, 4]")
print(f"{find_median([-5, -1, -3])} == [-5, -1, -3]")
print(f"{find_median([10, 2, 38, 23, 38, 23, 21])} == [10, 2, 38, 23, 38, 23, 21]")

print("4 - is_sorted_ascending(numbers)")
print(f"{is_sorted_ascending([])}, []")
print(f"{is_sorted_ascending([5])}, [5]")
print(f"{is_sorted_ascending([1, 2, 3, 4])}, [1, 2, 3, 4]")
print(f"{is_sorted_ascending([3, 1, 2])}, [3, 1, 2]")
print(f"{is_sorted_ascending([2, 2, 2])}, [2, 2, 2]")
print(f"{is_sorted_ascending([5, 4, 3, 2, 1])}, [5, 4, 3, 2, 1]")
print(f"{is_sorted_ascending([-3, -2, -1, 0, 1])}, [-3, -2, -1, 0, 1]")

print("5 - Söka efter element i en lista")
print(autocomplete_list("app", ["apple", "banana", "apricot", "orange"]))
print(autocomplete_list("ap", ["apple", "banana", "apricot", "orange"]))
print(autocomplete_list("", ["apple", "banana", "apricot", "orange"]))

print("6 - Multiplikationstabellen")
print("3 * 4 blir ==", multiplication_table(3,4))
try:
    print(multiplication_table(3,-1))
except ValueError as e:
    print(f"⚠️ Warning: {e}")
try:
    print(multiplication_table("a",1))
except TypeError as e:
    print(f"⚠️ Warning: {e}")

print("7 - Balansera listor")