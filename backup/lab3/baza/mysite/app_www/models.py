from django.db import models

# Model Stanowisko
class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100, blank=False, null=False)  # Pole wymagane, niepuste
    opis = models.TextField(blank=True, null=True)  # Pole opcjonalne

    def __str__(self):
        return self.nazwa

# Model Osoba
class Osoba(models.Model):
    PLEC_CHOICES = [
        ('K', 'Kobieta'),
        ('M', 'Mężczyzna'),
        ('I', 'Inne'),
    ]

    imie = models.CharField(max_length=50, blank=False, null=False)  # Pole wymagane, niepuste
    nazwisko = models.CharField(max_length=50, blank=False, null=False)  # Pole wymagane, niepuste
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES, blank=False, null=False)  # Pole wyboru
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)  # Klucz obcy do modelu Stanowisko

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
