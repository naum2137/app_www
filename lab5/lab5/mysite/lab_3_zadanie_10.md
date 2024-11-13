from app_www.models import Osoba, Stanowisko 

# 1. Wyświetl wszystkie obiekty modelu Osoba
osoby = Osoba.objects.all()

print(osoby)

# 2. Wyświetl obiekt modelu Osoba z id = 3
osoba_z_id_3 = Osoba.objects.get(id=3)

print(osoba_z_id_3)

# 3. Wyświetl obiekty modelu Osoba, których nazwisko rozpoczyna się na literę 'K'
osoby_na_k = Osoba.objects.filter(nazwisko__startswith='K')

print(osoby_na_k)

# 4. Wyświetl unikalną listę stanowisk przypisanych do modeli Osoba
unikalne_stanowiska = Osoba.objects.values_list('stanowisko', flat=True).distinct()

print(unikalne_stanowiska)

# 5. Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco
stanowiska_posortowane = Stanowisko.objects.order_by('-nazwa').values_list('nazwa', flat=True)

print(stanowiska_posortowane)

# 6. Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie
nowa_osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec=1, stanowisko=Stanowisko.objects.first())  # Zakładając, że stanowisko istnieje
nowa_osoba.save()
print("Nowa osoba została dodana:", nowa_osoba)
