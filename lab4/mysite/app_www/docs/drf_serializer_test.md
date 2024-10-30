# Testowanie serializerów Django REST Framework

## OsobaSerializer - Serializacja obiektu

```python
from app_www.models import Osoba
from app_www.serializers import OsobaSerializer

# Serializowanie obiektu Osoba
osoba = Osoba.objects.create(imie="Jan", nazwisko="Kowalski", plec="mężczyzna")
serializer = OsobaSerializer(osoba)
print(serializer.data)

```
## StanowiskoSerializer - Tworzenie nowego obiektu przy użyciu danych JSON

```python
from app_www.serializers import StanowiskoSerializer

# Dane do utworzenia nowego stanowiska
stanowisko_data = {"nazwa": "Programista", "opis": "Tworzenie oprogramowania"}
serializer = StanowiskoSerializer(data=stanowisko_data)

# Sprawdzamy, czy dane są prawidłowe i zapisujemy obiekt
if serializer.is_valid():
    serializer.save()
    print("Nowy obiekt Stanowisko został utworzony:", serializer.data)
else:
    print("Błędy walidacji:", serializer.errors)