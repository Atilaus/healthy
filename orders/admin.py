from django.contrib import admin
from .models import *

# Register your models here.
class ProductInOrderInline(admin.TabularInline):
	model = ProductInOrder
	extra = 0

class StatusAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Status._meta.fields]
	search_fields = ['name', 'email']
	list_display_links = [field.name for field in Status._meta.fields]

	class Meta:
		model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	search_fields = ['name', 'email']
	inlines = [ProductInOrderInline]
	list_display_links = [field.name for field in Order._meta.fields]

	class Meta:
		model = Order
admin.site.register(Order, OrderAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductInOrder._meta.fields]
	search_fields = ['name']
	list_display_links = [field.name for field in ProductInOrder._meta.fields]

	class Meta:
		model = ProductInOrder
admin.site.register(ProductInOrder, ProductInOrderAdmin)

class ProductInCartAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductInCart._meta.fields]
	search_fields = ['name']
	list_display_links = [field.name for field in ProductInCart._meta.fields]

	class Meta:
		model = ProductInCart
admin.site.register(ProductInCart, ProductInCartAdmin)