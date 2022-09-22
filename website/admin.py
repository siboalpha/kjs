from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'phone_number', 'date_time')