from django.contrib import admin
from .models import News, Category, Plant, Sale, PlantSale, Client, DeliveryAddress, Review, CartContent, Cart, Order, OrderComposition, Payment, Delivery

# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Plant)
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
