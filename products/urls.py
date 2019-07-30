from django.conf.urls import url, include
from products import views


urlpatterns = [
	#url('landing/', views.landing, name='landing')
	url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'), 
	#url(r'^product/', views.product, name='product'), 
]