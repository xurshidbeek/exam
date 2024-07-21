from django import forms
from cart.models import Fruit

class CourseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'description', 'price', 'taste', 'color']
