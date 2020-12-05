from django.urls import path

from books_api import views_hard_way
from books_api import views

urlpatterns = [
    # path('', views_hard_way.ListBookView.as_view(), name='list_books_api'),
    path('', views.BookListAPIView.as_view(), name='list_books_api'),
    # path('<int:pk>', views_hard_way.DetailsBookView.as_view(), name='details_books_api'),
    path('<int:pk>', views.BookDetailsAPIView.as_view(), name='details_books_api'),
]