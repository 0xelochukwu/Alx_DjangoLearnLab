from django.contrib import admin
from .models import UserProfile, Author, Book, Library

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'author__name')


admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Library)
