from django.urls import path
from .views import HomeView, ProductDetailView, checkout, add_to_cart, remove_from_cart

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart')
]