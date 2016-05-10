from django.contrib import admin
from django.contrib.auth.models import Group
from polls import models

from models import UserProfile
from models import UserGroup
from user_admin import UserProfileAdmin


class UserInline(admin.TabularInline):
    model = UserProfile
    readonly_fields = ['password','last_login']
class UserGroupAdmin(admin.ModelAdmin):
    inlines = [UserInline,]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserGroup,UserGroupAdmin)
admin.site.unregister(Group)