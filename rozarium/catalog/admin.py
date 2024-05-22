from django.contrib import admin
from .models import News, Category, Plant

#, Sale, PlantSale, Client, DeliveryAddress, Review, CartContent, Cart, Order, OrderComposition, Payment, Delivery

# Register your models here.
admin.site.register(News)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Plant, PlantAdmin)


'''
admin.site.register(Sale)
admin.site.register(PlantSale)
admin.site.register(Client)
admin.site.register(DeliveryAddress)
admin.site.register(Review)
admin.site.register(CartContent)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderComposition)
admin.site.register(Payment)
admin.site.register(Delivery)
'''
