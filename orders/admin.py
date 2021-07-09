from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','product','quantity','price')
    list_display_links = ('id','product')
    list_per_page = 50

class OrderAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'full_name')
    list_display = ('id', 'full_name', 'address',
                    'phone_number', 'email', 'completed', 'date_ordered')
    list_filter = ('date_ordered', 'completed',)
    search_fields = ('full_name', 'address', )
    list_per_page = 50
    


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)