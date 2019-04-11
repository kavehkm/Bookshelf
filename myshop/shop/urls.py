from django.urls import path
from shop import views



urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('category/<slug:category_slug>/books/', views.books_by_category, name='books_by_category'),
    path('book/<int:book_id>/<slug:book_slug>/', views.book_detail, name='book_detail'),
]