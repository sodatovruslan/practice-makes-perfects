from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Borrow

def book_list(request):
    books=Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, pk):
    book=get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def borrow_book(request, pk):
    book=get_object_or_404(Book, pk=pk)
    if book.quantity>0:
        Borrow.objects.create(user=request.user, book=book)
        book.quantity-=1
        book.save()
    return redirect('my_books')

def return_book(request, pk):
    borrow=get_object_or_404(Borrow, pk=pk)
    borrow.returned=True
    borrow.save()
    borrow.book.quantity+=1
    borrow.book.save()
    return redirect('my_books')


def my_books(request):
    borrows=Borrow.objects.filter(user=request.user)
    return render(request, 'library/my_books.html', {'borrows': borrows})


def book_create(request):
    if request.method=='POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            description=request.POST['description'],
            quantity=request.POST['quantity'],
            image=request.FILES.get('image'),
        )
        return redirect('book_list')
    return render(request, 'library/book_create.html')


def book_update(request, pk):
    book=get_object_or_404(Book, pk=pk)
    if request.method=='POST':
        book.title=request.POST['title']
        book.author=request.POST['author']
        book.description=request.POST['description']
        book.quantity=request.POST['quantity']
        if request.FILES.get('image'):
            book.image=request.FILES.get('image')
        book.save()
        return redirect('book_list')
    return render(request, 'library/book_edit.html', {'book': book})

    
def book_delete(request, pk):
    book=get_object_or_404(Book, pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_delete.html', {'book': book})  
