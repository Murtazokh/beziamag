from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('core.urls')), 
    path('products/', include('products.urls', namespace='products')), 
    path('orders/', include('orders.urls', namespace='orders')),  
    path('cart/', include('cart.urls', namespace='cart')),
]
