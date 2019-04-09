from django.shortcuts import render
from cart.cart import Cart
from orders.forms import OrderForm
from orders.models import Order, OrderItem



def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                Order.objects.create(
                    order=order,
                    book=item['book'],
                    price=item['price'],
                    quantity = item['quantity']
                )
            cart.clear()
            context = {'order': order}
            return render(request, 'orders/order_created.html', context)
    else:
        form = OrderForm()
    context = {
        'form': form,
        'cart': cart
    }
    return render(request, 'orders/order_create.html', context)
