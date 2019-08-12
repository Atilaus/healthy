from django.shortcuts import render
from products.models import *
from landing.models import BackgroundImage

# Create your views here.
def product(request, product_id):
	product = Product.objects.get(id=product_id)
	group_name = Product.objects.filter(category=product.category)
	
	product_group = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category=product.category)

	four_last_products = product_group.order_by('-id')[:4]
	print(four_last_products)
	
	
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	

	return render(request, 'products/product.html', locals())
