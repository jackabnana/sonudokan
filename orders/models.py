from django.db import models
from products.models import Product
from users.models import User
from .validators import validate_number
from django.utils.timezone import datetime

PAYMENT_METHOD = (
    ('esewa',"Esewa"),
    ("cod","Cash On Delivery")
)

class Order(models.Model):
    user = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=180)
    address = models.CharField(max_length=180)
    phone_number = models.CharField(
        max_length=10, validators=[validate_number])
    email = models.EmailField(max_length=254, blank=True)
    completed = models.BooleanField(default=False)
    date_ordered = models.DateField(default=datetime.now)
    payment_method = models.CharField(choices=PAYMENT_METHOD,default="cod", max_length=50)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id', ]
    
    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.order_items.all())
        return total_cost


class OrderItem(models.Model):
    user = models.ForeignKey(
        User, related_name="items", on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(
        Product, related_name="items", on_delete=models.CASCADE, null=True)
    order_detail = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.product.price * self.quantity