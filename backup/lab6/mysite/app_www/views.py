from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework import generics, filters

# Widoki dla Osoba (już istnieją, ale tutaj je przypominam)
class OsobaListCreate(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['imie', 'nazwisko']

class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

# Nowe widoki dla Stanowisko
class StanowiskoListCreate(generics.ListCreateAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

class StanowiskoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer
