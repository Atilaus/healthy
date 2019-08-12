from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from .models import *
#from django.contrib.auth.decorators import login_required


# Create your views here.


products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)

def landing(request):
	subscribe_form = SubscriberForm(request.POST or None)
	if request.method == "POST" and subscribe_form.is_valid():
		savingForm = subscribe_form.save()
	
	return render(request, 'landing/home.html', locals())

def milkproducts(request):
	products_images_milkproducts = products_images.filter(product__category__id=7)
	milkproducts_group = Product.objects.filter(category_id=7)
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return render(request, 'landing/milkproducts.html', locals())

def snacks(request):
	products_images_snacks = products_images.filter(product__category__id=6)
	snacks_group = Product.objects.filter(category_id=6)
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return render(request, 'landing/snacks.html', locals())

def juices(request):
	products_images_juices = products_images.filter(product__category__id=5)
	juices_group = Product.objects.filter(category_id=5)
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return render(request, 'landing/juices.html', locals())

def vegetables(request):
	products_images_vegetables = products_images.filter(product__category__id=3)
	juices_group = Product.objects.filter(category_id=3)
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return render(request, 'landing/vegetables.html', locals())
	
def fruits(request):
	products_images_fruits = products_images.filter(product__category__id=4)
	fruit_group = Product.objects.filter(category_id=4)
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return render(request, 'landing/fruits.html', locals())
	
def drinks(request):
	products_images_drinks = products_images.filter(product__category__id=1)
	drinks_group = Product.objects.filter(category_id=1)
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return render(request, 'landing/drinks.html', locals())
	
#@login_required	
def home(request):
	
	slider_images = ProductImage.objects.filter(is_active=True, is_slider=True, product__is_active=True)
	slick_slider = slider_images #if need to add some filter
	#last_eight_images = products_images.order_by('-id')[:8]
	products_images_drinks = products_images.filter(product__category__id=1)
	products_images_food = products_images.filter(product__category__id=2)
	four_products_images_drinks = products_images_drinks.order_by('-id')[:4]
	four_products_images_food = products_images_food.order_by('-id')[:4]
	
	last_eight_images = products_images.order_by('id')[:8]
	last_eight_in_ascending_order = reversed(last_eight_images)
	
	carousel_images = mainCarousel.objects.filter(is_active=True).order_by('id')[1:]
	main_carousel_image = mainCarousel.objects.filter(is_active=True, id = 1)
	
	bg_image = BackgroundImage.objects.filter(is_active=True)
	
	return render(request, 'landing/home.html', locals())