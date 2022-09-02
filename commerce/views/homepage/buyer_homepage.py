from django.contrib.postgres.search import SearchVector
from django.shortcuts import render

from commerce.models.book import Book


def buyer_homepage(request):
    books = Book.objects.all()
    return render(request, 'commerce/homepage/buyer/home.html', {'books': books})


def search_book(request):
    query = request.GET.get("q")
    books = Book.objects.annotate(search=SearchVector("title", "description", "author")).filter(
        search=query
    )
    return render(request, 'commerce/homepage/buyer/home.html', {'books': books})
