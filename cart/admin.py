from django.contrib import admin
from .models import Fruit

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'taste', 'weight', 'price', 'created_at', 'updated_at')  # Qanday maydonlar ko'rsatilishini belgilash
    search_fields = ('name', 'color', 'taste')  # Qidiruv uchun maydonlar
    prepopulated_fields = {'slug': ('name',)}  # Slug maydonini avtomatik to'ldirish
    ordering = ('-created_at',)  # Qanday tartibda ko'rsatilishini belgilash