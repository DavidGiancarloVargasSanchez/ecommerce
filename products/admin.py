from django.contrib import admin

# Register your models here.
from .models import Product, Category, Review

admin.register(Product)
admin.register(Category)
admin.register(Review)