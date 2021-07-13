from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

from .models import UpdateUser

# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'first_name','middle_name', 'surname', 'sex', 'phone', 'account_number', 'available_bal', 'status', 'transfer_amount', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'first_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)

class UpdateUserAdmin(admin.ModelAdmin):
  list_display = ('id', 'user_id', 'date_updated')
  list_display_links = ('id', 'user_id')
  search_fields = ('user_id',)
  list_per_page = 25

admin.site.register(UpdateUser, UpdateUserAdmin)