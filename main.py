from src.celsius_to_fahrenheit import c_to_f
from src.count_words import count_words
from src.find_median import find_median

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