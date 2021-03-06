from store.models.orders import Order
from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display= ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display= ['name']

class CustomerCategory(admin.ModelAdmin):
    list_display=['name','phone', 'email','password']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, CustomerCategory)
admin.site.register(Order)

