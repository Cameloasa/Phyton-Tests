#1a funktion, som omvandlar Celsius till Fahrenheit.
def c_to_f(degree):
    if degree < -273.15:
        return None
    return round(degree * 9 / 5 + 32, 2) #round()