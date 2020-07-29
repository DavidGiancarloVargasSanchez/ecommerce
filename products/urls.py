from django.urls import path
from .views import home, cat_prod, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('cat_prod/<str:category_id>', cat_prod, name='cat_prod'),
    path('product_detail/<str:product_id>', product_detail, name='product_detail')
]