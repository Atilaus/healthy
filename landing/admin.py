from django.contrib import admin
from .models import *

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Subscriber._meta.fields]
	list_display_links = ['email']
	search_fields = ['name', 'email']
	#inlines = [FieldMappingInline]
	#fields = []
	#exclude = ["type"]
	#list_filter = ('name',)
	#search_fields = ['category', 'subCategory', 'suggestKeyword']
	
	class Meta:
		model = Subscriber
	

admin.site.register(Subscriber, SubscriberAdmin)

class mainCarouselAdmin(admin.ModelAdmin):
	list_display = [field.name for field in mainCarousel._meta.fields]
	search_fields = ['name']
	list_display_links = [field.name for field in mainCarousel._meta.fields]

	class Meta:
		model = mainCarousel
admin.site.register(mainCarousel, mainCarouselAdmin)

class BackgroundImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in BackgroundImage._meta.fields]
	search_fields = ['name']
	list_display_links = [field.name for field in BackgroundImage._meta.fields]

	class Meta:
		model = BackgroundImage
admin.site.register(BackgroundImage, BackgroundImageAdmin)