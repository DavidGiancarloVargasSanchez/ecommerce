from django.urls import path
from .views import add_item

urlpatterns = [
    path('add_item/<str:product_id>', add_item, name='add_item')
]