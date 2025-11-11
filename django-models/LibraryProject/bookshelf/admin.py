from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # removed publication_year
    list_filter = ('author',)           # removed publication_year
    search_fields = ('title', 'author__name')  # author is a ForeignKey
