from django.contrib import admin
from .models import Book, Language, Genre, BookInstance, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
