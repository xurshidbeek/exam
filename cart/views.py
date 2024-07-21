from django.shortcuts import render, get_object_or_404
from .models import Fruit

def fruit_list(request):
    fruits = Fruit.objects.all()
    return render(request, 'shop.html', {'fruits': fruits})

def fruit_detail(request, slug):
    fruit = get_object_or_404(Fruit, slug=slug)
    return render(request, 'shop_detail.html', {'fruit': fruit})
