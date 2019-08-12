from .models import ProductInCart
from landing.models import BackgroundImage
from landing.forms import *


def bg_image_show(request):
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return locals()
	

def getting_cart_info(request):
	session_key = request.session.session_key
	if not session_key:
		request.session.cycle_key()
	
	products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
	products_total_nmb = products_in_cart.count()
	
	return locals()
	
def getting_subscribe_form(request):
	subscribe_form = SubscriberForm(request.POST or None)
	if request.method == "POST" and subscribe_form.is_valid():
		savingForm = subscribe_form.save()
	return locals()