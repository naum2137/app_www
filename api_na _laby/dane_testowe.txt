# kod wklej do shell'a
# 1.uruchom shell"a  "python manage.py shell"   najlepiej w projekcie tam gdzie znajduje się plik manage.py projektu
# lub dodaj odpowiednią lokalizację menage.py.
# 2.wklej poniższy kod.
# 3. gotowe
#   ___
#  d-_-b
#  -\ /-
#   ! !
#
# python manage.py shell


from app_zaliczenie.models import User, Book, Category, Rental, BookReservation
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, timedelta

# Tworzenie grup
admin_group, _ = Group.objects.get_or_create(name='admin')
user_group, _ = Group.objects.get_or_create(name='user')

# Dodanie uprawnień do grupy Admin
admin_permissions = Permission.objects.all()
admin_group.permissions.set(admin_permissions)

# Dodanie uprawnień do grupy User
# Tylko wybrane modele: Book, Rental, BookReservation
user_permissions = Permission.objects.filter(
    content_type__model__in=['book', 'rental', 'bookreservation'],
    codename__startswith='view'  # Użytkownik może przeglądać dane
)
user_group.permissions.set(user_permissions)

# Tworzenie użytkowników
admin_user = User.objects.create_user(
    username='admin',
    email='admin@example.com',
    password='admin123',
    is_staff=True,
    is_superuser=True
)
admin_user.groups.add(admin_group)

user1 = User.objects.create_user(
    username='user1',
    email='user1@example.com',
    password='user123'
)
user1.groups.add(user_group)

user2 = User.objects.create_user(
    username='user2',
    email='user2@example.com',
    password='user123'
)
user2.groups.add(user_group)

user3 = User.objects.create_user(
    username='user3',
    email='user3@example.com',
    password='user123'
)
user3.groups.add(user_group)

user4 = User.objects.create_user(
    username='user4',
    email='user4@example.com',
    password='user123'
)
user4.groups.add(user_group)

# Tworzenie użytkownika z dostępem do panelu admina, ale bez uprawnień superużytkownika
staff_user = User.objects.create_user(
    username='staff_user',
    email='staff_user@example.com',
    password='staff123',
    is_staff=True
)
staff_user.groups.add(user_group)

# Tworzenie kategorii
category_fiction = Category.objects.create(name="Fiction")
category_science = Category.objects.create(name="Science")
category_history = Category.objects.create(name="History")
category_philosophy = Category.objects.create(name="Philosophy")
category_technology = Category.objects.create(name="Technology")

# Tworzenie książek
books = [
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", description="A novel about the American dream.", category=category_fiction, available=True),
    Book(title="A Brief History of Time", author="Stephen Hawking", description="A book about cosmology.", category=category_science, available=True),
    Book(title="Sapiens: A Brief History of Humankind", author="Yuval Noah Harari", description="A book about the history of humanity.", category=category_history, available=False),
    Book(title="Meditations", author="Marcus Aurelius", description="Reflections of the Roman Emperor.", category=category_philosophy, available=True),
    Book(title="Clean Code", author="Robert C. Martin", description="A handbook of agile software craftsmanship.", category=category_technology, available=True),
    Book(title="To Kill a Mockingbird", author="Harper Lee", description="A novel about racial injustice.", category=category_fiction, available=False),
    Book(title="The Selfish Gene", author="Richard Dawkins", description="A book about evolutionary biology.", category=category_science, available=True),
    Book(title="The Art of War", author="Sun Tzu", description="An ancient Chinese military treatise.", category=category_philosophy, available=True),
]

for book in books:
    book.save()

# Tworzenie wypożyczeń
rentals = [
    Rental(user=user1, book=books[0], rental_date=datetime.now() - timedelta(days=5), return_date=None, status='active'),
    Rental(user=user2, book=books[1], rental_date=datetime.now() - timedelta(days=15), return_date=datetime.now() - timedelta(days=5), status='returned'),
    Rental(user=user3, book=books[2], rental_date=datetime.now() - timedelta(days=3), return_date=None, status='active'),
    Rental(user=user4, book=books[3], rental_date=datetime.now() - timedelta(days=30), return_date=datetime.now() - timedelta(days=1), status='returned'),
    Rental(user=user1, book=books[4], rental_date=datetime.now() - timedelta(days=10), return_date=None, status='active'),
]

for rental in rentals:
    rental.save()

# Tworzenie rezerwacji książek
reservations = [
    BookReservation(user=user1, book=books[5], reservation_date=datetime.now() - timedelta(days=10), expiration_date=datetime.now() + timedelta(days=10), status='active'),
    BookReservation(user=user2, book=books[6], reservation_date=datetime.now() - timedelta(days=20), expiration_date=datetime.now() - timedelta(days=5), status='expired'),
    BookReservation(user=user3, book=books[4], reservation_date=datetime.now() - timedelta(days=15), expiration_date=datetime.now() + timedelta(days=5), status='active'),
    BookReservation(user=user4, book=books[7], reservation_date=datetime.now() - timedelta(days=5), expiration_date=datetime.now() + timedelta(days=20), status='active'),
    BookReservation(user=user1, book=books[1], reservation_date=datetime.now() - timedelta(days=8), expiration_date=datetime.now() + timedelta(days=12), status='active'),
]

for reservation in reservations:
    reservation.save()

print("Rozszerzone dane testowe zostały pomyślnie utworzone!")
