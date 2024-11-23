from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from app_zaliczenie.models import Book, Category, Rental, BookReservation, User
from app_zaliczenie.serializers import BookSerializer, CategorySerializer, RentalSerializer, BookReservationSerializer, \
    UserRegistrationSerializer, UserSerializer
from .permissions import IsAdminGroup, IsUserGroup


class AdminOnlyView(APIView):
    permission_classes = [IsAdminGroup]

    def get(self, request):
        return Response({"message": "Tylko dla administratorów."})


class UserOnlyView(APIView):
    permission_classes = [IsUserGroup]

    def get(self, request):
        return Response({"message": "Tylko dla użytkowników."})


# Widok CRUD dla Książek
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Lista książek zaczynających się od podanej litery
    @action(detail=False, methods=['get'], url_path='startswith/(?P<letter>.+)')
    def startswith(self, request, letter=None):
        books = Book.objects.filter(title__istartswith=letter)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

# Widok CRUD dla Kategorii
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Widok CRUD dla Wypożyczeń
class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    # Zestawienie miesięczne wypożyczeń
    @action(detail=False, methods=['get'], url_path='monthly-summary/(?P<year>\d+)/(?P<month>\d+)')
    def monthly_summary(self, request, year=None, month=None):
        rentals = Rental.objects.filter(rental_date__year=year, rental_date__month=month).count()
        return Response({"month": month, "year": year, "total_rentals": rentals})

# Widok CRUD dla Rezerwacji
class BookReservationViewSet(viewsets.ModelViewSet):
    queryset = BookReservation.objects.all()
    serializer_class = BookReservationSerializer

    # Lista aktywnych rezerwacji dla użytkownika
    @action(detail=False, methods=['get'], url_path='active')
    def active_reservations(self, request):
        user = request.user
        reservations = BookReservation.objects.filter(user=user, status='active')
        serializer = self.get_serializer(reservations, many=True)
        return Response(serializer.data)


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # Pozwala na dostęp bez uwierzytelnienia

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #  widok tylko dla administratorów
    permission_classes = [IsAdminUser]

