from django.urls import path
from .views import  *


urlpatterns = [
    path('create/', create_book, name='create_book'),
    path('list/', list_books, name='list_books'),
    path('detail/<int:pk>/', book_detail, name='book_detail'),
]


