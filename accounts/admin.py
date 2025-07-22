from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_role')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)

    def get_role(self, obj):
        return obj.role
    get_role.short_description = 'Role'

admin.site.register(Profile, ProfileAdmin)
