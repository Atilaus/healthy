from django.conf.urls import url, include
from . import views


urlpatterns = [
	url('cart_adding/', views.cart_adding, name='cart_adding'),
	url('checkout/', views.checkout, name='checkout'),
	url('success/', views.success, name='success_url'),
	url('ordershistory/', views.userorders, name='orders_url'),
	
]