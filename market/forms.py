from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['category','name', 'description','price','image']
        widgets={
            'category':forms.Select(attrs={
                'class':'px-6 py-3 rounded-xl border border-gray-700 w-full appearance-none'
            }),
            'name':forms.TextInput(attrs={
                'class':'w-full rounded-xl px-6 py-3 border border-gray-700',
                'placeholder':'Name of the Item'

            }),
            'description':forms.Textarea(attrs={
                'placeholder':'Description about the Item',
                'class':'px-6 py-4 rounded-xl border border-gray-700 w-full'
            }),
            'price':forms.NumberInput(attrs={
                                'class':'w-full rounded-xl px-6 py-3 border border-gray-700',
                                'placeholder':'Amount of the Item'
            }),
            'image':forms.ClearableFileInput(attrs={
                                'class':'w-full rounded-xl px-6 py-3 border border-gray-700',
            }),
        }