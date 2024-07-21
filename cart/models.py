from django.db import models
from django.utils.text import slugify

class Fruit(models.Model):
    name = models.CharField(max_length=100)  # Mevaning nomi
    slug = models.SlugField(unique=True, max_length=100)  # URL uchun qabul qilingan matn
    color = models.CharField(max_length=50)  # Mevaning rangi
    taste = models.CharField(max_length=50)  # Mevaning ta'mi (misol: shirin, nordon)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Mevaning og'irligi (gramm)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Mevaning narxi (pul birligi)
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqti
    updated_at = models.DateTimeField(auto_now=True)  # Yangilangan vaqti
    description = models.CharField(max_length=200)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
