from msilib.schema import CustomAction
from pyexpat import model
from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustumUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']
            
admin.site.register(CustomUser, CustumUserAdmin)