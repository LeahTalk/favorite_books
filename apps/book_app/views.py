from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import datetime

def index(request):
    if 'curUser' not in request.session:
        return redirect('/')
    context = {
        'user' : Users.objects.get(email = request.session['curUser']),
        'books' : Books.objects.all()
    }
    return render(request, 'book_app/index.html', context)

def book_details(request, book_id):
    if 'curUser' not in request.session:
        return redirect('/')
    context = {
        'user' : Users.objects.get(email = request.session['curUser']),
        'book' : Books.objects.get(id = book_id)
    }
    return render(request, 'book_app/details.html', context)

def create_book(request):
    errors = Books.objects.book_validator(request.POST)
    if Books.objects.filter(title=request.POST['title']).exists():
        errors['exists'] = "A book with this title already exists!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    curUser = Users.objects.get(email = request.session['curUser'])
    Books.objects.create(title = request.POST['title'], desc = request.POST['desc'], 
                    uploaded_by = curUser)
    book = Books.objects.get(title = request.POST['title'])
    book.users.add(curUser)
    book.save()
    return redirect('/books')

def add_favorite(request, book_id):
    book = Books.objects.get(id = book_id)
    curUser = Users.objects.get(email = request.session['curUser'])
    book.users.add(curUser)
    book.save()
    return redirect('/books/favorites')

def edit_book(request, book_id):
    book = Books.objects.get(id = book_id)
    book.title = request.POST['title']
    book.desc = request.POST['desc']
    book.save()
    return redirect('/books/' + book_id)

def delete_book(request, book_id):
    book = Books.objects.get(id = book_id)
    book.delete()
    return redirect('/books')

def all_favorites(request):
    if 'curUser' not in request.session:
        return redirect('/')
    user = Users.objects.get(email = request.session['curUser'])
    context = {
        'user' : user,
        'books' : user.favorites.all()
    }
    return render(request, 'book_app/favorites.html', context)

def remove_favorite(request, book_id):    
    user = Users.objects.get(email = request.session['curUser'])
    book = Books.objects.get(id = book_id)
    user.favorites.remove(book)
    return redirect('/books/favorites')

