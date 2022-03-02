from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import *

# Register your models here.
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = (
    (None, {'fields': ('email', 'password', ('first_name', 'last_name'),)}),
    ('Contact', {
        # 'classes': ('collapse',),
        'fields': ('phone',)
    }),
    # ('Biographical Details', {
    #     # 'classes': ('collapse',),
    #     'fields': ('avatar',)
    # }),
    ('Permissions', {'fields': ( 'is_staff', 'is_active')}),
    # ('Group Permissions', {'fields': ('groups', 'user_permissions')}), if add permissions class
    # ('Time', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    model = CustomUser
    list_display = ['email', 'username','address']


admin.site.register(CustomUser, CustomUserAdmin)

