from django.contrib import admin
from .models import Profile
from customers.models import Client
# Register your models here.

admin.site.register(Profile)
admin.site.register(Client)