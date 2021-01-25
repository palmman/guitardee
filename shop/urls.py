from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop, name='shop'),
    path('<int:id>/', views.shop_single, name='shop_single'),
    path('cart/', views.cart, name='cart'),
]