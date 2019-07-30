from django.db import models

# Create your models here.
class ProductCategory(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	
	def __str__(self):
		return "%s" % (self.name)
	
	class Meta:
		verbose_name = 'Product Category'
		verbose_name_plural = 'Product Categories'

class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
	discount = models.IntegerField(default=0)
	category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
	short_description = models.TextField(blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	object = models.Manager()
	
	def __str__(self):
		return "%s, %s" % (self.price, self.name)


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='static/products_images')
	description = models.TextField(blank=True, null=True, default=None)
	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	object = models.Manager()
	
	def __str__(self):
		return "Image %s" % (self.id)
	
	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Images'