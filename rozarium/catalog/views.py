from django.shortcuts import render,  get_object_or_404
from .models import Category, Plant


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    plants = Plant.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        plants = plants.filter(category=category)
    return render(request,
                  'rozarium/plant/list.html',
                  {'category': category,
                   'categories': categories,
                   'plants': plants})

def product_detail(request, id, slug):
    plant = get_object_or_404(Plant,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'rozarium/plant/detail.html',
                  {'plant': plant})
