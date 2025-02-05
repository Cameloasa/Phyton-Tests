from src.celsius_to_fahrenheit import c_to_f
from src.count_words import count_words

print("Omvandla Celsius(°C) till Fahrenheit(°F)")
print(f"-273.15°C == {c_to_f(-273.15)}°F")
print(f"-274°C == {c_to_f(-274)}°F")
print(f"-40°C == {c_to_f(-40)}°F")
print(f"100°C == {c_to_f(100)}°F")

print("Returnerar antalet ord")
print(f"Antalet ord i('') ==" , count_words(""))
print(f"Antalet ord i(' ') ==" , count_words(" "))
print(f"Antalet ord i('hello') ==" , count_words("hello"))
print(f"Antalet ord i('hello world') ==" , count_words("hello world"))
print(f"Antalet ord i('  hello  world  ') ==" , count_words("  hello  world  "))
print(f"Antalet ord i('  hello  world    ! !') ==" , count_words("  hello  world    ! !"))