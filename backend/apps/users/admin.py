from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the admin panel
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('bio', 'avatar')}),
    )

    # Show these columns in the user list
    list_display = ['username', 'email', 'is_staff', 'date_joined']
    search_fields = ['username', 'email']