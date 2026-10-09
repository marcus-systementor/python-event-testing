# Introduktion till testing – Event

I måndagens event-labb skrev ni valideringsregler. Här är [event_system.py](event_system.py) redan färdig och korrekt. **Ändra inte den filen idag.** Nu ska ni beskriva och kontrollera dess beteende med enkla automatiserade tester i [test_event_system.py](test_event_system.py).

```text
måndag: skriv reglerna
tisdag: kontrollera reglerna med tester
```

Detta är en **kort självstudielabb**. Ni behöver bara `test_`-functions, vanlig `assert` och kommandot `python -m pytest`. Inga fixtures, mocks, testklasser eller medvetet felande tester behövs. Läs ett befintligt test, skriv ett liknande, kör och se att det blir grönt.

## Kom igång

Öppna en terminal i mappen som innehåller `README.md`. Installera [requirements.txt](requirements.txt) en gång i er Python-miljö:

```text
python -m pip install -r requirements.txt
```

Kör sedan testerna från **samma mapp**:

```text
python -m pytest -v
```

På Windows kan kommandona börja med `py` om `python` inte hittas; på vissa datorer används `python3`. Om `pytest` saknas, kontrollera att ni installerade med **samma** Python-kommando som ni använder för att köra testerna. Ändra en sak i taget och kör igen.

`make_event()` och `make_attendee()` högst upp i testfilen skapar ny testdata. Anropa dem i varje nytt test så att testet börjar med ett känt `state` och inte är beroende av ett tidigare test. Ändra inte dessa helpers.

## Steg 1 – installera

**Mål:** Få tillgång till `pytest`. **Gör:** Kör installationskommandot ovan. **Klar när:** Kommandot avslutas utan fel. Detta behöver normalt bara göras en gång i miljön.

## Steg 2 – kör de färdiga testerna

**Mål:** Se ett grönt testresultat. **Gör:** Kör `python -m pytest -v`. **Klar när:** Alla åtta starttester visar `PASSED`. Det betyder att resultatet stämde med testets förväntning. Gå inte vidare förrän alla passerar. Om något inte fungerar, kontrollera först terminalens mapp och Python-kommandot; ändra inte applikationskoden.

## Steg 3 – läs ett enkelt test

**Mål:** Förstå vad `assert` kontrollerar. **Gör:** Hitta detta test i testfilen:

```python
def test_is_valid_age_rejects_negative_age():
    assert is_valid_age(-1) is False
```

`test_` gör att `pytest` hittar functionen. `is_valid_age(-1)` är anropet vi provar. `is False` är det förväntade svaret. `assert` kontrollerar förväntningen. **Klar när:** Du kan förklara testet med egna ord och peka ut dess rad i den gröna listan.

## Steg 4 – läs ett test av `state`

**Mål:** Se att ett operationstest kan kontrollera både `return` och förändrat `state`. **Gör:** Läs `test_book_ticket_changes_state_when_booking_succeeds()` i testfilen. Där kontrolleras `result is True`, att `tickets_left` blivit `4` och att `has_ticket` blivit `True`. Läs också testet för nekad bokning: då ska inget relevant `state` ändras. **Klar när:** Du kan säga varför ett korrekt `return`-värde ensamt inte räcker för att kontrollera bokningen.

## Steg 5 – testa `has_entry_pass()`

**Mål:** Skriva dina första egna tester. **Gör:** Lägg till tre separata `test_`-functions längst ned i testfilen. Använd en ny `attendee` i varje test. Prova: bara biljett → `True`, bara guest pass → `True`, varken biljett eller guest pass → `False`. Följ mönstret i ålderstesterna men skriv dina egna `assert`-rader. **Klar när:** `python -m pytest -v` visar dina tre nya tester som `PASSED`.

## Steg 6 – testa `can_enter_event()`

**Mål:** Beskriva flera inträdesregler med enkla tester. **Gör:** Skriv minst tre separata tester med nya `event` och `attendee` varje gång: ett tillåtet inträde, ett nekat inträde och ett gränsfall där `age == minimum_age`. Ge personen biljett eller guest pass när det behövs. Som nekat fall kan du välja för låg ålder, saknat ID, cancelled event eller saknat entry pass. Tänk ut förväntat bool-svar före körningen. **Klar när:** Alla tre nya tester visar `PASSED`.

## Steg 7 – testa `can_check_in()`

**Mål:** Skilja ett tillåtet check-in-försök från ett redan genomfört. **Gör:** Skriv minst två tester: en person med giltigt pass och ID som inte är checked in → `True`; samma förutsättningar men `is_checked_in = True` → `False`. Kontrollera gärna också att validation-anropet inte ändrade `is_checked_in`. **Klar när:** Båda testerna passerar och du kan förklara varför functionen inte själv ändrar `state`.

## Steg 8 – testa `cancel_event()`

**Mål:** Kontrollera både `return` och `state` för en operation. **Gör:** Skriv minst två tester. Vid första cancellation: förvänta `True`, `is_cancelled = True` och `is_event_open = False`. Vid andra cancellation: anropa functionen två gånger på **samma event** och förvänta `False` andra gången, utan någon ny förändring av eventets `state`. Skriv koden själv med mönstret från bokningstesterna. **Klar när:** Båda testerna passerar.

## Steg 9 – kör hela samlingen

**Mål:** Kontrollera att du har beskrivit alla åtta application functions. **Gör:** Kör `python -m pytest -v` och läs listan. Starttesterna täcker `is_valid_age()`, `can_book_ticket()`, `book_ticket()` och `check_in()`. Dina tester ska dessutom täcka `has_entry_pass()`, `can_enter_event()`, `can_check_in()` och `cancel_event()`. **Klar när:** Alla tester visar `PASSED`. Ingen coverage-mätning behövs. Gör gärna en liten `commit`, till exempel `Add event validation tests`.

## Steg 10 – kort reflektion

**Mål:** Sätta ord på vad du nyss gjorde. **Gör:** Svara kort, gärna tillsammans med en kurskamrat:

1. Vad gör `assert`?
2. Vad betyder ett `PASSED` test?
3. Varför testar vi både `return`-värde och `state`?
4. Varför använder varje test nya `event`- och `attendee`-dictionaries?
5. Vad är skillnaden mellan valideringen i `event_system.py` och testerna i `test_event_system.py`?

**Klar när:** Du kan förklara ett eget test utan att läsa det rad för rad. Om du är klar: använd resten av självstudietiden till repetition av validering och tidigare Pythonmoment.

Idag har koden varit korrekt från början och testerna har bekräftat beteendet. På nästa lärarledda lektion arbetar vi vidare med vad som händer när kod förändras och varför tester blir särskilt värdefulla då.

## Facit

I mappen `facit/` finns en komplett version av testfilen.

Försök först skriva testerna själv innan du jämför med facit. Flera korrekta testlösningar kan finnas. Facit är ett exempel på en lösning, inte den enda tillåtna lösningen.
