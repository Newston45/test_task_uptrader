from django import forms
from django.contrib import admin
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)
