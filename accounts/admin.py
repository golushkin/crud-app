from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CutomUserChangeForm, CutomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CutomUserCreationForm
    form = CutomUserChangeForm
    model = CustomUser
    list_display = ['email','username','date','is_staff']


admin.site.register(CustomUser,CustomUserAdmin)
