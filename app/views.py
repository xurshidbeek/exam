from django.shortcuts import render
from cart.models import Fruit

def home_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'index.html')



def cart_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'cart.html')


def checout_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'chackout.html')


def contact_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'contact.html')


def shop_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'shop.html')


def shop_detail_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'shop-detail.html')


def testimonial_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, 'testimonial.html')


def ntfound_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        fruits = Fruit.objects.filter(tittle__icontains=search) | Fruit.objects.filter(
            author__first_name__icontains=search)
        if fruits:
            return render(request, 'main/base.html', {'fruit': fruits, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'main/base.html', {'message': "NOt found"})

    return render(request, '404.html')
