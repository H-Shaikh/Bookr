from django.shortcuts import render

from .models import Book
from .utils import average_rating


def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})


def book_list(request):
    books = Book.objects.all()
    books_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        books_list.append({'book': book,
                           'book_rating': book_rating,
                           'number_of_reviews': number_of_reviews})

    context = {
        'books_list': books_list
    }
    return render(request, 'reviews/book_list.html', context)
