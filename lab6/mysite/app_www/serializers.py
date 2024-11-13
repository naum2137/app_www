
from rest_framework import serializers
from .models import Osoba, Stanowisko

# 1. Klasa serializera dziedzicząca po `serializers.Serializer`
class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=100)
    nazwisko = serializers.CharField(max_length=100)
    plec = serializers.ChoiceField(choices=[(1, "Kobieta"), (2, "Mężczyzna"), (3, "Inne")], required=True)
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())  # Zmienione na queryset

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance

# 2. ModelSerializer dla Stanowisko
class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']
