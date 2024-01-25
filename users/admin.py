from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_filter = ('groups',)  # Добавляем фильтр по полю 'groups'

admin.site.register(User, UserAdmin)
# @admin.register(User)
# class VersionAdmin(admin.ModelAdmin):
#     list_display = ('email', 'is_verified', 'verification_token','is_active',)
#     list_filter = ('is_verified',)