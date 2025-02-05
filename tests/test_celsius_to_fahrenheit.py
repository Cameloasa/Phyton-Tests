
from src.celsius_to_fahrenheit import c_to_f

#1a Hitta på lämplig testdata till följande funktion,
#som omvandlar Celsius till Fahrenheit.
def test_c_to_f():
    assert c_to_f(0) == 32  # 0°C = 32°F
    assert c_to_f(-40) == -40 # -40°C = -40°F
    assert c_to_f(100) == 212  # 100°C = 212°F
    assert c_to_f(-273.15) == -459.67 # min temp -459.67 - aprox()
    assert c_to_f(-274) is None

"""
1b Vilka ekvivalensklasser har parametern degree?
mindre -274
exakt -273.15
temp negativ -40
temp positiv 100
"""