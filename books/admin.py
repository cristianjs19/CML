from django.contrib import admin

from books.models import Book, LendingAgreement, LendingRequest


class BookAdmin(admin.ModelAdmin):
	list_display = ('user', 'author', 'title')
	search_fields = ('user', 'author', 'title')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class LendingRequestAdmin(admin.ModelAdmin):
    search_fields = ['user', 'title']
    list_display = ['user', 'title']

class LendingAgreementAdmin(admin.ModelAdmin):
    search_fields = ['user', 'book']
    list_display = ['user', 'book']


admin.site.register(Book, BookAdmin)
admin.site.register(LendingRequest, LendingRequestAdmin)
admin.site.register(LendingAgreement, LendingAgreementAdmin)