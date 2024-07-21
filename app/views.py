from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def cart_view(request):
    return render(request, 'cart.html')


def checout_view(request):
    return render(request, 'chackout.html')


def contact_view(request):
    return render(request, 'contact.html')


def shop_view(request):
    return render(request, 'shop.html')


def shop_detail_view(request):
    return render(request, 'shop-detail.html')


def testimonial_view(request):
    return render(request, 'testimonial.html')


def ntfound_view(request):
    return render(request, '404.html')
