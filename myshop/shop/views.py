from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Category, Book
from cart.forms import CartAddBookForm



def book_list(request):
    categories = Category.objects.all().values('name', 'slug')
    books = Book.objects.filter(available=True).values('id', 'title', 'slug', 'image').order_by('-created')
    context = {
        'categories': categories,
        'books': books
    }
    return render(request, 'shop/book_list.html', context)


def books_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all().values('name', 'slug')
    books = Book.objects.filter(category=category).values('id', 'title', 'slug', 'image')
    context = {
        'category': category,
        'categories': categories,
        'books': books
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
