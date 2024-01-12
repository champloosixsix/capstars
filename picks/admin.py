from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Picks

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "verified_member"]
    list_editable = ['verified_member']

class CustomPicksAdmin(admin.ModelAdmin):
    model = Picks
    list_display = ["pick", "outcome", "closed"]
    list_display_links = ["pick"]
    list_editable = ['closed', 'outcome']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Picks, CustomPicksAdmin)