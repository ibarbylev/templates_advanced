from django.urls import path

from books_api import views

urlpatterns = [
    path('', views.index, name='')
]