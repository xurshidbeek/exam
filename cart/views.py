from django.shortcuts import render, get_object_or_404
from .models import Fruit
from django.contrib.auth.decorators import login_required

def fruit_list(request):
    fruits = Fruit.objects.all()
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'shop.html', {'fruits': fruits})
@login_required()
def fruit_detail(request, slug):
    fruit = get_object_or_404(Fruit, slug=slug)
    return render(request, 'shop_detail.html', {'fruit': fruit})
