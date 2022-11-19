from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books_ = Book.objects.values()
    books = []
    for row in books_:
        books.append({})
        books[-1]["name"] = row["name"]
        books[-1]["author"] = row["author"]
        books[-1]["pub_date"] = row["pub_date"]

    context = {"books": books}
    return render(request, template, context)


def page_view(request):
    sorted_books = Book.objects.values().order_by("pub_date")
    numb_page = request.GET.get("page", 1)
    paginator = Paginator(sorted_books, 1)
    page = paginator.get_page(numb_page)
    try:
        if page.has_next:
            next_page = str(sorted_books[page.next_page_number() - 1]["pub_date"])
        else:
            next_page = '<-- Назад'
    except:
        next_page = '<-- Назад'
    try:
        if page.has_previous:
            prev_page = str(sorted_books[page.previous_page_number() - 1]["pub_date"])
        else:
            prev_page = 'Вперёд -->'
    except:
        prev_page = 'Вперёд -->'

    context = {"page": page,
               "next_page": next_page,
               "prev_page": prev_page,
               }
    template = 'books/page_list.html'
    return render(request, template, context)
