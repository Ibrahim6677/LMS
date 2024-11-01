from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'retal_price_day',
            'rental_peroiod',
            'total_rental',
            'status',
            'category',
        ]
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'author': forms.TextInput(attrs={'class': 'form-control'}),
          'photo_book': forms.FileInput(attrs={'class': 'form-control'}),
          'photo_author': forms.FileInput(attrs={'class': 'form-control'}),
          'pages': forms.NumberInput(attrs={'class': 'form-control'}),
          'price': forms.NumberInput(attrs={'class': 'form-control'}),
          'retal_price_day': forms.NumberInput(attrs={'class': 'form-control', 'id': 'retal_price'}),
          'rental_peroiod': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rental_days'}),
          'total_rental': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_rental'}),
          'status': forms.Select(attrs={'class': 'form-control'}),
          'category': forms.Select(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            
        ]
        widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control'}),
        }