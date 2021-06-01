from .models import Books
from django.forms import ModelForm,TextInput,Textarea

class BooksForm(ModelForm):
    class Meta:
        model= Books
        fields=['title','subtitle','description','price','genre','author','year']

widgets={
    "title":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Название статьм'
    }),
        "subtitle":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'anons статьм'
    }),
        "description":Textarea(attrs={
        'class': 'form-control',
        'placeholder':'anons статьм'
    }),
        "price":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Text статьм'
    }),
        "genre":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'anons статьм'
    }),
        "author":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'anons статьм'
    }),
        "year":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'anons статьм'
    }),
}
