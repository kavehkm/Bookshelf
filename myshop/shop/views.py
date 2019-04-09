from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Category, Book
from cart.forms import CartAddBookForm



def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available=True).order_by('-created')
    books_count = books.count()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'books': books,
        'books_count': books_count
    }
    return render(request, 'shop/book_list.html', context)


def book_detail(request, book_id, book_slug):
    book = get_object_or_404(Book, id=book_id, slug=book_slug, available=True)
    form = CartAddBookForm()
    context = {
        'book': book,
        'form': form
    }
    return render(request, 'shop/book_detail.html', context)
