# Wypożyczalnia Książek Django

## Wprowadzenie

  
Aplikacja pozwala na zarządzanie użytkownikami, książkami, kategoriami, wypożyczeniami i rezerwacjami.  
Dokumentacja obejmuje modele, endpointy API oraz szczegóły dotyczące uprawnień.

---

## Modele

### 1. Użytkownik (User)  
Model niestandardowego użytkownika dziedziczącego po `AbstractUser`.

- **Pola:**
  - `username`: Nazwa użytkownika.
  - `email`: Adres e-mail użytkownika.
  - `password`: Hasło (przechowywane w formie hashu).
  - `is_staff`: Czy użytkownik ma dostęp do panelu administratora.
  - `is_superuser`: Czy użytkownik ma pełne uprawnienia administracyjne.

---

### 2. Książka (Book)  
Model reprezentujący książki dostępne do wypożyczenia.

- **Pola:**
  - `title`: Tytuł książki.
  - `author`: Autor książki.
  - `description`: Opis książki.
  - `category`: Kategoria (relacja FK do `Category`).
  - `available`: Czy książka jest dostępna do wypożyczenia.

---

### 3. Kategoria (Category)  
Model kategorii książek.

- **Pola:**
  - `name`: Nazwa kategorii (unikalna).

---

### 4. Wypożyczenie (Rental)  
Model śledzący wypożyczenia książek.

- **Pola:**
  - `user`: Użytkownik wypożyczający książkę (relacja FK do `User`).
  - `book`: Wypożyczona książka (relacja FK do `Book`).
  - `rental_date`: Data wypożyczenia.
  - `return_date`: Data zwrotu (może być pusta).
  - `status`: Status wypożyczenia (np. "active", "returned").

---

### 5. Rezerwacja Książki (BookReservation)  
Model rezerwacji książek.

- **Pola:**
  - `user`: Użytkownik dokonujący rezerwacji (relacja FK do `User`).
  - `book`: Rezerwowana książka (relacja FK do `Book`).
  - `reservation_date`: Data dokonania rezerwacji.
  - `expiration_date`: Data wygaśnięcia rezerwacji.
  - `status`: Status rezerwacji (np. "active", "expired", "cancelled").

---

## Endpointy API

### 1. Uwierzytelnianie
- **POST `/api/token/`**: Uzyskanie tokenów dostępu i odświeżania.
- **POST `/api/token/refresh/`**: Odświeżenie tokenu dostępu.

---

### 2. Książki (Books)
- **GET `/books/`**: Pobranie listy wszystkich książek.
- **POST `/books/`**: Dodanie nowej książki (tylko dla administratorów).
- **GET `/books/{id}/`**: Pobranie szczegółowych informacji o książce.
- **PUT `/books/{id}/`**: Aktualizacja danych książki (tylko dla administratorów).
- **DELETE `/books/{id}/`**: Usunięcie książki (tylko dla administratorów).
- **GET `/books/startswith/{letter}/`**: Pobranie książek zaczynających się na podaną literę.

---

### 3. Kategorie (Categories)
- **GET `/categories/`**: Pobranie listy wszystkich kategorii.
- **POST `/categories/`**: Dodanie nowej kategorii (tylko dla administratorów).
- **GET `/categories/{id}/`**: Pobranie szczegółowych informacji o kategorii.

---

### 4. Wypożyczenia (Rentals)
- **GET `/rentals/`**: Pobranie listy wszystkich wypożyczeń (tylko dla administratorów).
- **POST `/rentals/`**: Utworzenie nowego wypożyczenia.
- **GET `/rentals/monthly-summary/{year}/{month}/`**: Zestawienie miesięczne wypożyczeń.

---

### 5. Rezerwacje (Reservations)
- **GET `/reservations/`**: Pobranie listy wszystkich rezerwacji (tylko dla administratorów).
- **POST `/reservations/`**: Utworzenie nowej rezerwacji.
- **GET `/reservations/active/`**: Pobranie aktywnych rezerwacji zalogowanego użytkownika.

---

## Uprawnienia

### 1. Grupa Admin
- Pełny dostęp do wszystkich endpointów i funkcji administracyjnych.

---

### 2. Grupa User
- Dostęp ograniczony do:
  - Tworzenia wypożyczeń i rezerwacji.
  - Przeglądania swoich aktywnych rezerwacji.

---
