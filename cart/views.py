from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from django.contrib import messages
from django.http import HttpResponseRedirect

@require_POST
def cart_add(request, product_id):
    route = request.META.get('HTTP_REFERER','')
    cart = Cart(request)
    data = request.POST
    id = data["id"]
    product = get_object_or_404(Product, id=id)
    cart.add(
        product=product,
        quantity=data['quantity'],
        override_quantity=False
    )
    messages.success(request,f"{product.name} added to the cart!")
    if route:
        return HttpResponseRedirect(route)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    route = request.META.get('HTTP_REFERER','')
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.error(request,f"{product.name} removed the cart!")
    if route:
        return HttpResponseRedirect(route)
    return redirect('cart:cart_detail')


def cart_handle(request):
    cart = Cart(request)
    data = request.POST
    ids = data.getlist('ids')
    quantities = data.getlist('quantities')
    for index, item_id in enumerate(ids):
        product = get_object_or_404(Product, pk=item_id)
        cart.add(
            product=product,
            quantity=quantities[index],
            override_quantity=True)
    messages.success(request,f"Cart Value successfully updated!")
    return redirect('cart:cart_detail')


def cart_detail(request):
    return render(request, 'cart/cart.html')
