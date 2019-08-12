from django.db import models

# Create your models here.
class Subscriber(models.Model):
	email = models.EmailField()
	#name = models.CharField(max_length=40)
	
	def __str__(self):
		return "%s" % (self.email)
		
	class Meta:
		verbose_name = 'Subscriber'
		verbose_name_plural = 'Subscribers'
		
class mainCarousel(models.Model):
	name = name = models.CharField(max_length=64, blank=True, null=True, default=None, db_index=True)
	description = models.TextField(blank=True, null=True, default=None)
	image = models.ImageField(upload_to='static/img_carousel')
	is_active = models.BooleanField(default=True)
	
	def __str__(self):
		return "Image %s, %s" % (self.id, self.name)
	
	class Meta:
		verbose_name = 'Carousel Image'
		verbose_name_plural = 'Main Carousel Images'
		
class BackgroundImage(models.Model):
	name = name = models.CharField(max_length=64, blank=True, null=True, default=None, db_index=True)
	description = models.TextField(blank=True, null=True, default=None)
	image = models.ImageField(upload_to='static/bg_images')
	is_active = models.BooleanField(default=False)
	
	def __str__(self):
		return "Image %s, %s" % (self.id, self.name)
	
	class Meta:
		verbose_name = 'BG Image'
		verbose_name_plural = 'Background Images'