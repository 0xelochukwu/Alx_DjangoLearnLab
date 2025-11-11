from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Book

# Permission check function
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

# View for listing books
@user_passes_test(is_librarian, raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Queryset variable 'books'
    return render(request, 'bookshelf/book_list.html', {'books': books})
