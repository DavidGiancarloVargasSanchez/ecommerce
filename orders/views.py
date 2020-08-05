from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from users.models import Customer
from orders.models import OrderItem, Order
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order_qs = Order.objects.filter(customer=request.user.customer, complete=False) 
    if order_qs.exists():
        order = order_qs[0]
        #Check whether the order item is in the order
        order_item_qs = order.orderitem_set.filter(product__id=product_id)
        if order_item_qs.exists():
            order_item = order_item_qs[0]
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated to your cart")
        else:
            order.orderitem_set.create(product=product)
            order.save()
            messages.info(request, "This item was added to your cart")
    else:
        order = Order.objects.create(user=request.user.customer)
        order.orderitem_set.create(product=product)
        order.save()
        messages.info(request, "This item was added to your cart")
    
    order_items = OrderItem.objects.all()
    context = {
        'order_items': order_items
    }
    return render(request, 'order_item.html', context=context)
