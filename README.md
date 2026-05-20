# Mini_Library_Project


A simple Object-Oriented Programming (OOP) based Library Management System developed in Python.

This project demonstrates the use of:

- Classes and Objects
- Encapsulation
- Properties
- Exception Handling
- Type Hinting
- Modular Programming
- Clean and Readable Code Structure

---

# Features

- Add Books
- Register Members
- Borrow Books
- Return Books
- View All Books
- View All Members
- View Loan Records
- Custom Exception Handling

---

# Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

# Project Structure

```text
Library-Management-System/
│
├── main.py
├── library_service.py
├── book.py
├── member.py
├── loan.py
├── exception.py
└── README.md
```

---

# Class Overview

## Book Class

Represents a book inside the library.

### Attributes
- `book_id`
- `title`
- `author`
- `is_available`

### Methods
- `borrow()`
- `return_book()`

---

## Member Class

Represents a registered library member.

### Attributes
- `member_id`
- `name`
- `email`

---

## Loan Class

Represents a borrowing transaction.

### Attributes
- `loan_id`
- `book`
- `member`
- `is_active`

### Methods
- `close_loan()`

---

## LibraryService Class

Handles all library operations.

### Methods
- `add_book()`
- `register_member()`
- `borrow_book()`
- `return_book()`
- `view_books()`
- `view_members()`
- `view_loans()`

---

# Custom Exceptions

The system uses custom exception handling for better error management.

```python
class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass

class BookUnavailableError(LibraryError):
    pass
```

---

# How to Run

## Step 1
Open terminal or command prompt.

## Step 2
Navigate to the project folder.

```bash
cd Library-Management-System
```

## Step 3
Run the program.

```bash
python main.py
```

---

# Sample Output

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. View Loans
8. Exit
```

---

# Example Workflow

## Add Book

```text
Book ID: B01
Title: Python Basics
Author: John Doe
```

## Register Member

```text
Member ID: M01
Name: Angelo
Email: angelo@email.com
```

## Borrow Book

```text
Book ID: B01
Member ID: M01
Loan ID: L01
```

---

# OOP Concepts Used

| Concept | Implementation |
|----------|----------------|
| Encapsulation | Private attributes using `__` |
| Abstraction | Service-based operations |
| Modularity | Separate Python files |
| Reusability | Reusable classes and methods |
| Exception Handling | Custom exception classes |

---

# Improvements Added

- Clean code structure
- Proper indentation
- Type hints
- Custom exceptions
- Readable method naming
- Object-oriented architecture

---

# Author

Developed by Angelo Gosim.