from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from models import UserProfile
from models import UserGroup
from user_admin import UserProfileAdmin
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserGroup)
admin.site.unregister(Group)