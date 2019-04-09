from django.urls import path
from orders import views



urlpatterns = [
    path('create/', views.create_order, name='create_order'),
]