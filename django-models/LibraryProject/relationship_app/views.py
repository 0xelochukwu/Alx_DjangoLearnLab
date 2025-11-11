from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

from .models import Book
from .models import Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ✅ User Registration View
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


# ✅ User Login (Using Django’s Built-in LoginView)
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


# ✅ User Logout (Using Django’s Built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
