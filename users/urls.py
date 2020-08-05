from django.urls import path
from .views import register_page

urlpatterns = [
    path('register_page/', register_page, name='register'),
]

