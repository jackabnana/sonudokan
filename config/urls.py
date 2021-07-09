from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProductSitemap, ShopSitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap

sitemaps = {
    ProductSitemap.name: ProductSitemap,
    ShopSitemap.name: ShopSitemap,
    'flatpages':FlatPageSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('control-admin/', admin.site.urls),
    path('robots.txt',include('robots.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('compare/', include('compare.urls', namespace='compare')),
    path('', include('shops.urls', namespace="shops")),
    path('summernote/', include('django_summernote.urls')),
    path('products/', include('products.urls', namespace="products")),
    path('orders/', include('orders.urls', namespace="orders")),
    path('account/', include('users.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('info/', include('core.urls', namespace="core")),
    path('about/', include('django.contrib.flatpages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
