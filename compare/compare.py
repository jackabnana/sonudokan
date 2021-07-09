from django.conf import settings
from products.models import Product
from decimal import Decimal


class Compare(object):

    def __init__(self, request):
        self.session = request.session
        compare = self.session.get(settings.COMPARE_SESSION_ID)
        if not compare:
            compare = self.session[settings.COMPARE_SESSION_ID] = []

        self.compare = compare
        

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.compare:
            self.compare.append(product_id)
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        index = self.compare.index(product_id)
        self.compare.pop(index)
        self.save()

    def items(self):
        products = Product.objects.filter(id__in=self.compare)
        return products

    def __len__(self):
        return len(self.compare)

    def clear(self):
        self.session[settings.COMPARE_SESSION_ID] = []
        self.save()

