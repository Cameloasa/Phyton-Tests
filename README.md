1 Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?


1 Vilka ekvivalensklasser har uttrycken?
1a. x > 100
1b. y == 42
1c. len(text) >= 5
1d. z == True
1e. 8 < v < 16
1f. w == 32 or w == 64 or w == 128
1g. if x < 5: … elif x < 10: … elif x < 15: … else


2 Det har smugit sig in kommentarer i stället för kod på några ställen. Skriv färdigt testfallen test_empty_list och test_number_list.
# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

def test_empty_list():
    expected = # ???
    actual   = # ???
    assert actual == expected
    
def test_number_list():
    assert sum_list([5]) == 5
    assert # ???
    assert # ???
    assert # ???


3a Diskutera följande kod. Räcker det med ett testfall för att testa funktionen?
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return None

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.


4 Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något
def find_max(list):


5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. Formulera testfall för en funktion som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
def find_2nd_max(list):



2 Öva på TDD
Samla ihop dina funktioner så att de ligger i en eller flera moduler. Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32

1b Vilka ekvivalensklasser har parametern degree?

1c Skriv ett testfall.


2a Betrakta funktionen count_words(sentence), som tar en sträng och returnerar antalet ord. Ett ord är en serie tecken som separeras av mellanslag. Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.

2b Skriv testfall som testar alla AK.

2c Implementera funktionen, så att alla testfall blir gröna.


3a Betrakta funktionen find_median(numbers), som tar en lista med tal och returnerar medianen. Median är det mittersta talet, t.ex. är medianen 2 för listan [1, 2, 1000]. Om listan har jämnt antal element ska funktionen returnera medelvärdet av de två mittersta talen. Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.

3b Skriv testfall som testar alla AK.

3c Implementera funktionen, så att alla testfall blir gröna.


4 Betrakta funktionen is_sorted_ascending(numbers). Den ska returnera True om listan numbers är sorterad i stigande ordning, False annars.
4a Vilka ekvivalensklasser har numbers?
4b Formulera krav och acceptanskriterier för funktionen.
4c Skriv testfall för funktionen.



Söka efter användare
Tänk dig en funktion som kan användas för att visa sökresultat medan användaren skriver i ett sökfält. Funktionen ska ta två parametrar: input är det användaren skriver, master_list är en lista med alternativ som kan hittas.
def autocomplete_list(input, master_list):

Börja med att formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
Välj sedan ut ett AK och skriv ett testfall. (red)
Skriv sedan kod som uppfyller testfallet. (green)
Städa i koden, så du känner dig nöjd med din kod hittills. Fortsätt sedan med nästa AK.


Multiplikationstabellen
Vi behöver en funktion som kan ge oss multiplikationstabellen.
Parametern "n" talar om vilket tals tabell vi ska skapa.
Parametern "limit" talar om var vi ska sluta.
Om vi till exempel frågar efter 3:ans tabell, med limit==4, ska programmet räkna ut:
3*1 = 3
3*2 = 6
3*3 = 9
3*4 = 12

multiplication_table(3, 4) → [3, 6, 9, 12]

def muliplication_table(n, limit):
    return None  # TODO

Formulera krav och acceptanskriterier.
Kör sedan red-green-refactor för varje acceptanskriterium.


Balansera listor
Som en del i ett större program har vi en lista som kan innehålla flera element. Men elementen kan flyttas mellan denna och en annan lista. Vi behöver ett sätt att balansera listorna, så att de har lika många element - åtminstone så nära som möjligt. Ordningen på elementen är inte viktig.

Formulera krav och acceptanskriterier.

Kör sedan red-green-refactor för varje acceptanskriterium.
