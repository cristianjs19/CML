from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
	list_display = ('username','name', 'surname','is_staff')
	search_fields = ('username',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)



