from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from decimal import Decimal, InvalidOperation

def create_book(request):
    if request.method == "POST":
        name = request.POST.get("name")
        genre = request.POST.get("genre")
        price = request.POST.get("price")
        photo = request.FILES.get("photo")

        try:
            price = Decimal(price)
        except (InvalidOperation, TypeError):
            return HttpResponse('❌ Narx noto‘g‘ri formatda kiritildi!')

        book = Book(name=name, genre=genre, price=price, photo=photo)
        book.save()
        return HttpResponse(f'✅ Kitob qo‘shildi: {name}, {genre}, {price}')

    return render(request, 'products/create.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'products/list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'products/detail.html', {'book': book})




