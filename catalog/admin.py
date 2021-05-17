from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance,Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class AuthorAdmin(admin.ModelAdmin):

    pass
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    pass

class BookInstanceAdmin(admin.ModelAdmin):
    pass