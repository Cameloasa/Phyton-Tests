"""
AK
✔Ett ord definieras som en sekvens av tecken separerade med mellanslag (" ").
✔ Om meningen är tom (""), ska den returnera 0.
✔ Om meningen bara har mellanslag, ska den returnera 0.
✔ Orden kan separeras av ett eller flera mellanslag.
✔ Funktionen ska ignorera mellanslag i början och slutet.
✔ Den ska fungera för meningar med ett enda ord eller flera.
"""
from src.count_words import count_words


def test_count_words():
    assert count_words("") == 0
    assert count_words("  ") == 0
    assert count_words("hello") == 1
    assert count_words("hello world") == 2
    assert count_words("  hello  world  ") == 2
    assert count_words("  hello  world    ! !") == 4