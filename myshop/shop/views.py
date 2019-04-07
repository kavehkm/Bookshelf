from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Category, Book



def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available=True).order_by('-created')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'books': books
    }
    return render(request, 'shop/book_list.html', context)


def book_detail(request, book_id, book_slug):
    book = get_object_or_404(Book, id=book_id, slug=book_slug, available=True)
    context = {'book': book}
    return render(request, 'shop/book_detail.html', context)
