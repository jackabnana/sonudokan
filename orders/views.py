from django.shortcuts import get_object_or_404, reverse, redirect,render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from products.models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages
from core.mail import email
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

def payment_page(request,id):
    order = get_object_or_404(Order, id=id)
    return render(request,"orders/payment_processing.html",{"order":order})

def verify_esewa_payment(request,id):
    order = get_object_or_404(Order, id=id)
    import xml.etree.ElementTree as ET
    import requests
    oid = request.GET.get("oid")
    amt = request.GET.get("amt")
    refId = request.GET.get("refId")

    url = "https://esewa.com.np/epay/transrec"
    d = {
        'amt': amt,
        'scd': 'NP-ES-TRADE',
        'rid': refId,
        'pid': oid,
    }
    resp = requests.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == "Success":
        order.paid = True
        order.payment_method = "esewa"
        order.save()
        messages.success(request,"You have successfully paid the amount using eSewa.")
        return redirect("/")
    else:
        return redirect(reverse('payment_page',args=(order.id,)))


@login_required
def status(request, pk):
    order = get_object_or_404(OrderItem, pk=pk)
    if order.product.shop.owner == request.user:
        order.completed = not order.completed
        order.save()
    return redirect(reverse("core:dashboard"))


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = "orders/order_form.html"
    model = Order
    fields = [ "full_name",
              "address", "phone_number", "email","payment_method"]
    success_url = "products:detail"

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['email'] = self.request.user.email
        initial['phone_number'] = self.request.user.phone
        initial['address'] = self.request.user.address
        initial['full_name'] = self.request.user.first_name + \
            " " + self.request.user.last_name
        return initial

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        data = super().get_context_data(**kwargs)
        data["product"] = get_object_or_404(Product, pk=self.kwargs['pk'])
        return data

    def form_valid(self, form):
        self.object = form.save(commit=False)
        product = Product.objects.get(pk=self.kwargs['pk'])

        order = Order.objects.create(user=self.request.user,full_name=self.object.full_name,address=self.object.address, phone_number=self.object.phone_number,email=self.object.email)

        OrderItem.objects.create(user=self.request.user,product=product,order_detail=order,quantity=1,price=product.price)

        subject = f"New Order Received for {product.name}"
        message = f"""
        {self.object.full_name} placed an order of {product.name} \n
        Order Details: \n
        Quantity - 1
        By - {self.object.full_name} 
        Address - {self.object.address} 
        Number - {self.object.phone_number} 
        Email - {self.object.email} 

        * Please Visit https://tradenpl.com/info/dashboard to manage orders and see its detail.
        """
        email(product.shop.owner.email, subject, message)
        if self.object.payment_method == "esewa":
            return redirect(reverse("orders:payment_page",args=(order.id,)))
        messages.success(
            self.request, 'Your order was successfully added. The seller or brand will contact you soon.')
        return redirect(reverse(self.success_url, kwargs={"pk": product.pk, "slug": product.slug}))


class CartOrderCreateView(LoginRequiredMixin, CreateView):
    template_name = "orders/cart_order_form.html"
    model = Order
    fields = ["full_name",
              "address", "phone_number", "email","payment_method"]
    success_url = "shops:home"

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial['email'] = self.request.user.email
        initial['phone_number'] = self.request.user.phone
        initial['address'] = self.request.user.address
        initial['full_name'] = self.request.user.first_name + \
            " " + self.request.user.last_name
        return initial


    def form_valid(self, form):
        cart = Cart(self.request)
        self.object = form.save(commit=False)
        order = Order.objects.create(user=self.request.user,full_name=self.object.full_name,address=self.object.address, phone_number=self.object.phone_number,email=self.object.email)

        for item in cart:
            product = item["product"]
            quantity = item["quantity"]
            price = item["price"]

            OrderItem.objects.create(user=self.request.user,product=product,order_detail=order,quantity=quantity,price=price)

        cart.clear()

        if self.object.payment_method == "esewa":
            return redirect(reverse("orders:payment_page",args=(order.id,)))
        else:
            messages.success(self.request, 'Your order was successfully added. The seller or brand will contact you soon.')
        return redirect(reverse(self.success_url))
