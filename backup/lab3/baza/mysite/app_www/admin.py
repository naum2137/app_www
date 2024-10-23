from django.contrib import admin
from .models import Osoba, Stanowisko

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko']

@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
