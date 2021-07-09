from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils import timezone
from products.models import Product

class User(AbstractUser):
    """Custom User Model"""
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField(blank=True, null=True,validators=[MinValueValidator(9000000000)])
    address = models.CharField(max_length=100, default="", blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    is_seller = models.BooleanField(default=False, blank=True)


class Wishlist(models.Model):
    user = models.ForeignKey(
        User, related_name="wishlists", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Wishlist {self.id}"
