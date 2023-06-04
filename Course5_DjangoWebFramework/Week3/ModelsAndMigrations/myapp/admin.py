# myapp/admin.py

from django.contrib import admin

# Import the models from models.py
from .models import DrinksCategory, Drinks

# Register your models here.
admin.site.register(DrinksCategory)
admin.site.register(Drinks)