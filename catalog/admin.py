from django.contrib import admin

# Register your models here.
from .models import Book, Genre, BookInstance, Author, Language

#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

#admin.site.register(Author)

#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass
    list_display = ('first_name','last_name','date_of_birth','date_of_death')

#Register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)

#Register the admin classes for Book using a decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
    list_display = ('title','author','display_genre')


#Register the admin classes for BookInstance using a decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass




