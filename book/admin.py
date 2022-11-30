from django.contrib import admin

from book.models import Book, Author, BookAuthor, BookReview


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'isbn']


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
