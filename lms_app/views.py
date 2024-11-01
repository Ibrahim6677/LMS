from django.shortcuts import redirect, render
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.

# Home page view
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        add_category = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        
        if add_category.is_valid():
            add_category.save()
    
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'booksold': Book.objects.filter(status="sold").count(),
        'bookrented': Book.objects.filter(status="Rented").count(),
        'bookavailable': Book.objects.filter(status="Available").count(),
    }
    return render(request, 'pages/index.html', context)

# Books page view
def books(request):
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'category_form': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'book': book_id,
        'form': BookForm(instance=book_id),
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request, 'pages/delete.html', {'book': book_id})