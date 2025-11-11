from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these columns in list view
    list_filter = ('publication_year', 'author')            # add filters by year and author
    search_fields = ('title', 'author')                     # enable search by title or author
