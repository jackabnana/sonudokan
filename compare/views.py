from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .compare import Compare
from django.contrib import messages


def compare_add(request, product_id):
    compare = Compare(request)
    product = get_object_or_404(Product, id=product_id)
    compare.add(
        product=product
    )
    messages.success(request,f"{product.name} added to the compare list!")
    return redirect('compare:compare_detail')


def compare_remove(request, product_id):
    compare = Compare(request)
    product = get_object_or_404(Product, id=product_id)
    compare.remove(product)
    messages.error(request,f"{product.name} removed the compare!")
    return redirect('compare:compare_detail')

def clear_compare(request):
    compare = Compare(request)
    compare.clear()
    messages.error(request,f"Cleared the compare list!")
    return redirect('compare:compare_detail')

def compare_detail(request):
    compare = Compare(request)
    return render(request, 'compare/compare.html',{"items":compare.items()})
