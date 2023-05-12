from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from main_app.models import Profile, DateIdeas, Pfp, PotentialMatch

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(DateIdeas)
admin.site.register(Pfp)
admin.site.register(PotentialMatch)