from django.shortcuts import render
from django.http import request
from .models import Product, Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    category_product = Category.objects.get(name='Appliances')
    products = category_product.product_set.all()

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', context=context)

def cat_prod(request, category_id):
    categories = Category.objects.all()
    category_product = Category.objects.get(id=category_id)
    products = category_product.product_set.all()

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', context=context)

def product_detail(request, product_id):
    categories = Category.objects.all()
    product = Product.objects.get(id=product_id)

    context = {
        'categories': categories,
        'product': product
    }
    return render(request, 'product_detail.html', context=context)

    
    




#categories = Category.objects.all()
 #   category_result = {'categories': categories}
 #   products = Product.objects.all()
 #   product_result = {'prosucts': products}
 #   return render(request, 'index.htma', context=product_resutl)
 #   #return render(request, 'index.html', context=category_result)