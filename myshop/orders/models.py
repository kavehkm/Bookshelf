from django.db import models
from shop.models import Book



class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    tell = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    additional_info = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):
        return "%d" % self.id



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='items', on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return int(self.price) * self.quantity

