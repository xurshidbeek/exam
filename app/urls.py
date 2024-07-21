from django.urls import path,include
from .views import home_view, shop_view, shop_detail_view, checout_view, cart_view, contact_view, testimonial_view, ntfound_view
urlpatterns=[
    path('',home_view,name='home'),
    path('shop/', shop_view, name='shop'),
    path('shop_detail/', shop_detail_view, name='shop_detail'),
    path('check/', checout_view, name='check'),
    path('cart/', cart_view, name='cart'),
    path('contact/', contact_view, name='contact'),
    path('testimonial/', testimonial_view, name='testimonial'),
    path('404/', ntfound_view, name='notfound'),
]