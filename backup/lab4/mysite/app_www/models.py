from django.db import models

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

    class Meta:
        ordering = ['nazwisko']  # Sortowanie po nazwisku rosnąco

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
