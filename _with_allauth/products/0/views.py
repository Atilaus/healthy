from django.shortcuts import render
from products.models import *

# Create your views here.
def product(request, product_id):
	
	product = Product.object.get(id=product_id)
	return render(request, 'products/product.html', locals())