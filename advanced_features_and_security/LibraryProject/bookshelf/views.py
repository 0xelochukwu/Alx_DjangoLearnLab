from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from .models import Book

# Permission check function
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Secure view for listing books with search
@user_passes_test(is_librarian, raise_exception=True)
def book_list(request):
    query = request.GET.get('search', '')  # Get search input safely
    if query:
        # Use ORM with Q objects to prevent SQL injection
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    
    return render(request, 'bookshelf/book_list.html', {'books': books})
