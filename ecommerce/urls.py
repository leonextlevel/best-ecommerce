from django.contrib import admin
from django.urls import path, include
from ecommerce.product.views import hello_world

urlpatterns = [
    path('', hello_world),
    path('admin/', admin.site.urls),
    path('product/', include('ecommerce.product.urls')),
]
