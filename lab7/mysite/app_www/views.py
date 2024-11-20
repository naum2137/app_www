from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework import generics, filters
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from rest_framework.permissions import DjangoModelPermissions
from .permissions import CustomDjangoModelPermissions






# Widoki dla Osoba (już istnieją, ale tutaj je przypominam)
class OsobaListCreate(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['imie', 'nazwisko']

# Nowe widoki rozdzielone dla PUT i DELETE
class OsobaUpdateView(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OsobaDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Wymagane uwierzytelnienie tokenem

    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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

    class OsobaList(APIView):
        permission_classes = [permissions.IsAuthenticated]  # Tylko dla zalogowanych użytkowników

        def get(self, request, format=None):
            osoby = Osoba.objects.filter(wlasciciel=request.user)  # Filtrowanie po wlascicielu
            serializer = OsobaSerializer(osoby, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = OsobaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(wlasciciel=request.user)  # Ustawienie wlasciciela na aktualnie zalogowanego użytkownika
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StanowiskoMembersView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Wymagane uwierzytelnienie tokenem

    def get(self, request, pk, format=None):
        try:
            stanowisko = Stanowisko.objects.get(pk=pk)
        except Stanowisko.DoesNotExist:
            raise Http404

        osoby = Osoba.objects.filter(stanowisko=stanowisko)  # Filtracja osób przypisanych do stanowiska
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def osoba_view(request, pk):
    # Pobierz obiekt Osoba
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika o id={pk}.")

    # Sprawdź, czy użytkownik ma uprawnienie `can_view_other_persons`
    if not request.user.has_perm('app_www.can_view_other_persons') and osoba.wlasciciel != request.user:
        raise PermissionDenied()

    # Jeśli wszystko OK, wyświetl dane osoby
    return HttpResponse(f"Ten użytkownik nazywa się {osoba.imie} {osoba.nazwisko}")


class OsobaListCreateView(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    permission_classes = [CustomDjangoModelPermissions]

class OsobaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    permission_classes = [DjangoModelPermissions]