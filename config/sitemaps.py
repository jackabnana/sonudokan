from django.contrib.sitemaps import Sitemap
from shops.models import Shop
from products.models import Product
from django.urls import reverse

class ProductSitemap(Sitemap):
    name = 'product'
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Product.objects.order_by('id')
    
  

class ShopSitemap(Sitemap):
    name = 'shop'
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Shop.objects.order_by('id')
    
  
