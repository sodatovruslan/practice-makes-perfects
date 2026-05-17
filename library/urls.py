from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('borrow/<int:pk>/', views.borrow_book, name='borrow_book'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
    path('my-books/', views.my_books, name='my_books'),
    path('book-create/', views.book_create, name='book_create'),
    path('book-edit/<int:pk>/', views.book_update, name='book_edit'),
    path('book-delete/<int:pk>/', views.book_delete, name='book_delete'),
]
