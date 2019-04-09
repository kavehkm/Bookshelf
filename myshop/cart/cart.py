from django.conf import settings
from shop.models import Category, Book



class Cart(object):


    def __init__(self, request):
        """
        initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    

    def add(self, book, quantity=1, update_quantity=False):
        """
        add a book to cart or update its quantity.
        """
        book_id = str(book.id)
        if book_id not in self.cart.keys():
            self.cart[book_id] = {
                'quantity': 0,
                'price': book.price
            }
        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()
    

    def remove(self, book):
        """
        remove a book from cart.
        """
        book_id = str(book.id)
        if book_id in self.cart.keys():
            del self.cart[book_id]
            self.save()
    

    def save(self):
        """
        save items into session.
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    

    def __iter__(self):
        """
        iterate over items in the cart.
        """
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book
        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['quantity'] * item['price']
            yield item
    

    def __len__(self):
        """
        count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
    

    def get_total_price(self):
        """
        get total price for items in the cart.
        """
        return sum(item['quantity'] * int(item['price']) for item in self.cart.values())
    

    def clear(self):
        """
        clear cart
        """
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
