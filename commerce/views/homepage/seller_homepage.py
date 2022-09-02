from django.shortcuts import render

from commerce.models.book import Book
from commerce.utils.custom_decorators import is_seller


@is_seller()
def seller_homepage(request):
    books = Book.objects.all()
    return render(request, 'commerce/homepage/seller/home.html', {'books': books})
