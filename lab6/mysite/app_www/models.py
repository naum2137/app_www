from django.db import models
from django.contrib.auth.models import User  # Import modelu User
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100, blank=False, null=False)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        KOBIETA = 1, 'Kobieta'
        MEZCZYZNA = 2, 'Mężczyzna'
        INNE = 3, 'Inne'

    imie = models.CharField(max_length=50, blank=False, null=False)
    nazwisko = models.CharField(max_length=50, blank=False, null=False)
    plec = models.IntegerField(choices=Plec.choices, blank=False, null=False)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)
    wlasciciel = models.ForeignKey(User, on_delete=models.CASCADE, related_name="osoby")

    class Meta:
        ordering = ['nazwisko']  # Sortowanie po nazwisku rosnąco

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    def clean(self):
        # Walidacja dla pola `imie` i `nazwisko` - tylko litery
        if not re.match("^[A-Za-z]+$", self.imie):
            raise ValidationError("Imię może zawierać tylko litery.")
        if not re.match("^[A-Za-z]+$", self.nazwisko):
            raise ValidationError("Nazwisko może zawierać tylko litery.")

        # Walidacja dla `data_dodania` - nie może być z przyszłości
        if self.data_dodania and self.data_dodania > timezone.now().date():
            raise ValidationError("Data dodania nie może być z przyszłości.")
