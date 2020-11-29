from django.urls import path

from pythons_auth import views

urlpatterns = [
    path('login/', views.login_views, name='login_view'),
    path('logout/', views.logout_views, name='logout_view'),
]
