from src.autocomplete_list import autocomplete_list

"""
AK
✅ Returnera en lista med förslag som börjar med texten användaren har matat in.
✅ Var okänslig för gemener och versaler (spelar ingen roll om bokstäverna är stora eller små).
✅ Returnera en tom lista om det inte finns några matchningar.
✅ Hantera en tom inmatning (returnerar hela listan).
✅ Hantera en tom lista med alternativ (returnerar tom lista).
"""

def test_autocomplete_list():
    master_list = ["apple", "banana", "apricot", "orange"]

    expected = ["apple", "apricot"]
    actual = autocomplete_list("ap", master_list)

    assert expected == actual

def test_exact_match():
    expected = ["apple"]
    actual = autocomplete_list("apple", ["apple", "banana", "apricot", "orange"])

    assert expected == actual

def test_partial_match():
    expected = ["apple", "apricot"]
    actual = autocomplete_list("ap",["apple", "banana", "apricot", "orange"])

    assert expected == actual

def test_empty_input():
    expected = ["apple", "banana", "apricot", "orange"]
    actual = autocomplete_list("", ["apple", "banana", "apricot", "orange"])

    assert expected == actual

def test_empty_master_list():
    expected = []
    actual = autocomplete_list("ap", [])

    assert expected == actual

def test_sensitive_case():
    expected = ["Apple"]
    actual = autocomplete_list("App", ["Apple", "banana", "Apricot"])

    assert expected == actual
