from django.urls import path

from pythons_auth import views

urlpatterns = [
    path('login/', views.login_views, name='login_user'),
    path('logout/', views.logout_views, name='logout_user'),
]
