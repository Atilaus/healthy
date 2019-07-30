from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from products.models import Product
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
from landing.models import BackgroundImage



# Create your views here.
def cart_adding(request):
	return_dict = dict()
	session_key = request.session.session_key
	#print(request.POST)
	data = request.POST
	product_id = data.get("product_id")
	nmb = data.get("nmb")
	price = data.get("price")
	image_url = data.get("image_url")
	is_delete = data.get("is_delete")
	
	if is_delete == 'true':
		ProductInCart.objects.filter(id=product_id).update(is_active=False)
	else:
		new_product, created = ProductInCart.objects.get_or_create(session_key=session_key, product_id=product_id, image_url=image_url, is_active=True, defaults={"nmb": nmb})
		if not created:
			new_product.nmb += int(nmb)
			new_product.save(force_update=True)
	
	#common code for two cases
	products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
	products_total_nmb = products_in_cart.count()
	return_dict["products_total_nmb"] = products_total_nmb
	
	return_dict["products"] = list()
	for item in products_in_cart:
		product_dict = dict()
		product_dict["id"] = item.id
		product_dict["name"] = item.product.name
		product_dict["price_per_item"] = item.price_per_item
		product_dict["nmb"] = item.nmb
		product_dict["image_url"] = item.image_url
		product_dict["total_price"] = item.nmb * item.price_per_item
		return_dict["products"].append(product_dict)		
		
	return JsonResponse(return_dict)
	
def checkout(request):
	session_key = request.session.session_key
	products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True).exclude(order__isnull=False)
	form = CheckoutContactForm(request.POST or None)
	if request.POST:
		
		if form.is_valid():
			data = request.POST
			name = data["name"]
			phone = data["phone"]
			email = data["email"]
			
			user, created = User.objects.get_or_create(username=email, defaults={"first_name": name})
			print(data)
			order=Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)
			
			for name, value in data.items():
				if name.startswith("product_in_cart_"):
					product_in_cart_id = name.split("product_in_cart_")[1]
					
					product_in_cart = ProductInCart.objects.get(id=product_in_cart_id)
					print(product_in_cart)
					#product_in_cart.image_url = image_url
					print(product_in_cart.image_url)
					product_in_cart.nmb = value
					product_in_cart.order = order
					product_in_cart.save(force_update=True)

					
					ProductInOrder.objects.create(product=product_in_cart.product, nmb= product_in_cart.nmb, image_url = product_in_cart.image_url, price_per_item=product_in_cart.price_per_item, total_price=product_in_cart.total_price, order=order)
					
	bg_image = BackgroundImage.objects.filter(is_active=True)
				
	return render(request, 'orders/checkout.html', locals())
