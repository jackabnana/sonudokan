from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order, OrderItem
from shops.models import Shop
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    try:
        shop = Shop.objects.get(owner=request.user)
        products = shop.products.all().order_by('-id')
        dokan_orders = OrderItem.objects.filter(product__shop=shop).order_by('completed')
    except Exception:
        shop = None
        products = None
        dokan_orders = None
    context = {
        'orders': request.user.orders.all(),
        'dokanOrders': dokan_orders,
        'shop': shop,
        'products': products
    }
    return render(request, "core/dashboard.html", context)
