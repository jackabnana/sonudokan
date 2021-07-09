from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('status/<int:pk>/', views.status, name="status"),
    path('create/<int:pk>/', views.OrderCreateView.as_view(), name="order_create"),
    path('cart-create/', views.CartOrderCreateView.as_view(), name="cart_order_create"),
    path('payment-page/<int:id>/',views.payment_page, name="payment_page"),
    path('verify-esewa-payment/<int:id>/',views.verify_esewa_payment,name="verify_esewa"),
]
