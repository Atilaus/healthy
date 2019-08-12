from django.conf.urls import url, include
from landing import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url('fruits/', views.fruits, name='fruits_url'),
	url('vegetables/', views.vegetables, name='vegetables_url'),
	url('juices/', views.juices, name='juices_url'),
	url('snacks/', views.snacks, name='snacks_url'),
	url('drinks/', views.drinks, name='drinks_url'),
	url('milkproducts/', views.milkproducts, name='milkproducts_url'),
	#url('landing/', views.landing, name='landing')
]