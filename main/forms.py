from .models import Books
from django.forms import ModelForm,TextInput,Textarea

class BooksForm(ModelForm):
    class Meta:
        model= Books
        fields=['title','subtitle','description','price','genre','author','year']

widgets={
    "title":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Китептин аталышы'
    }),
        "subtitle":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Кыскача аныктама'
    }),
        "description":Textarea(attrs={
        'class': 'form-control',
        'placeholder':'Китепти сүрөттөө'
    }),
        "price":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Китептин баасы'
    }),
        "genre":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Жанры'
    }),
        "author":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Автору'
    }),
        "year":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Чыккан жылы'
    }),
}
