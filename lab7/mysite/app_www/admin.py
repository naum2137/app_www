from django.contrib import admin
from .models import Osoba, Stanowisko

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ['nazwa']  # Dodanie filtru dla pola nazwa

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_display', 'data_dodania']
    list_filter = ['plec', 'stanowisko', 'data_dodania']  # Dodanie filtrów dla stanowiska i daty utworzenia
    search_fields = ['imie', 'nazwisko']

    @admin.display(description='Stanowisko (id)')
    def stanowisko_display(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_display', 'data_dodania']
    list_filter = ['plec', 'stanowisko', 'data_dodania']  # Dodanie filtrów dla stanowiska i daty utworzenia
    search_fields = ['imie', 'nazwisko']

    @admin.display(description='Stanowisko (id)')
    def stanowisko_display(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ['nazwa']  # Dodanie filtru dla pola nazwa

