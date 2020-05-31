from django.contrib import admin

from books.models import Book, LendingAgreement


class BookAdmin(admin.ModelAdmin):
	list_display = ('user', 'author', 'title')
	search_fields = ('user', 'author', 'title')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class LendingAgreementAdmin(admin.ModelAdmin):
    search_fields = ['user', 'book']
    list_display = ['user', 'book']

# class PublicRequestAdmin(admin.ModelAdmin):
#     search_fields = ['user', 'book_name']
#     list_display = ['user', 'book_name']


admin.site.register(Book, BookAdmin)
admin.site.register(LendingAgreement, LendingAgreementAdmin)
# admin.site.register(PublicRequest, PublicRequestAdmin)