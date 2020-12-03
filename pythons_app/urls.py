from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.IndexListView.as_view(), name="index"),
    path('create/', views.create, name="create")
]
