from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='auth'),

    path('gethint', views.gethint, name='get-hint'),

    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
