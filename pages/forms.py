from django import forms 
from .models import Repair, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('title', 'image', 'date')
