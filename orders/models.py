from django.db import models
from products.models import Product
#from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
#from utils.main import disable_for_loaddata

# Create your models here.
class Status(models.Model):
	name = models.CharField(max_length=24, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Status %s" % self.name

	class Meta:
		verbose_name = 'Order Status'
		verbose_name_plural = 'Order Statuses'


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, default=None)
	customer_email = models.EmailField(blank=True, null=True, default=None)
	customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
	customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
	customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
	comments = models.TextField(blank=True, null=True, default=None)
	total_price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
	status = models.ForeignKey(Status, on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "Order %s %s %s" % (self.id, self.customer_name, self.status.name)

	def save(self, *args, **kwargs):
		super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
	#image_url = models.SlugField(blank=True, null=True, default=None)
	image_url = models.ImageField(blank=True, null=True, default=None)
	order = models.ForeignKey(Order,  on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='relatedorder')
	product = models.ForeignKey(Product,  on_delete=models.PROTECT, blank=True, null=True, default=None)

	customer_email = models.EmailField(blank=True, null=True, default=None)
	customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
	customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
	nmb = models.IntegerField(default=1)
	price_per_item = models.DecimalField(default=0, max_digits=9, decimal_places=2)
	total_price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	

	def __str__(self):
		return "Product %s %s %s" % (self.id, self.product.name, self.created)

	class Meta:
		verbose_name = 'Product in Order'
		verbose_name_plural = 'Products in Order'

	def save(self, *args, **kwargs):
		price_per_item = self.product.final_price
		self.price_per_item = price_per_item
		self.total_price = int(self.nmb) * price_per_item

		super(ProductInOrder, self).save(*args, **kwargs)

#@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
	order = instance.order
	all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

	order_total_price = 0
	for item in all_products_in_order:
		order_total_price += item.total_price

	instance.order.total_price = order_total_price
	instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInCart(models.Model):
	session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
	image_url = models.SlugField(blank=True, null=True, default=None)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True, default=None)
	nmb = models.IntegerField(default=1)
	price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	

	def __str__(self):
		return "Product %s %s %s" % (self.id, self.product.name, self.created)

	class Meta:
		verbose_name = 'Product in Cart'
		verbose_name_plural = 'Products in Cart'

	def save(self, *args, **kwargs):
		price_per_item = self.product.final_price
		self.price_per_item = price_per_item
		self.total_price = int(self.nmb) * price_per_item

		super(ProductInCart, self).save(*args, **kwargs)
