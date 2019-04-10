from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'tell', 'province', 'city', 'created', 'update', 'paid']
    list_filter = ['paid', 'created', 'update']
    inlines = [OrderItemInline]



admin.site.register(Order, OrderAdmin)
