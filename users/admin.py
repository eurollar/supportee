from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('type',)}),
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS


admin.site.register(CustomUser, CustomUserAdmin)
