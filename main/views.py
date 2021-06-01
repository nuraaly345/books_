from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Books
from .forms import BooksForm

def home(request):
    return render(request, 'home.html')

def page_book(request):
    book_list=Books.objects.all()
    return render(request, 'news.html', {'book_list': book_list})

def add_book(request):

    if request.method=='POST':
        form=BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-book')

    form=BooksForm()
    data={
        'form': form
    } 
    return render(request, 'forma.html', data)
  


def delete_book(request, id):
    book=Books.objects.get(id=id)
    book.delete()
    return redirect(page_book)

def mark_book(request, id):
    book=Books.objects.get(id=id)
    book.is_favorite=True
    book.save()
    return redirect(page_book)

def unmark_book(request, id):
    book=Books.objects.get(id=id)
    book.is_favorite=False
    book.save()
    return redirect(page_book)


def open_book(request, id):
    book_list=Books.objects.get(id=id)
    return render(request, 'detail_book.html',  {'book_list': book_list})

def contact(request):
    return render(request, 'contact.html')

