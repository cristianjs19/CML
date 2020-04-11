from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
	list_display = ('user', 'author', 'title')
	search_fields = ('user', 'author', 'title')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Book, BookAdmin)