from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem, Shipment

admin.register(Order)
admin.register(OrderItem)
admin.register(Shipment)
