from django.contrib import admin

from users.models import User


admin.site.register(User)
# @admin.register(User)
# class VersionAdmin(admin.ModelAdmin):
#     list_display = ('email', 'is_verified', 'verification_token','is_active',)
#     list_filter = ('is_verified',)