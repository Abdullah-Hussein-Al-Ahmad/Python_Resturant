from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2.html/', views.index2, name='index2'),
    path('home/', views.home, name='arabicfood'),
    path('login/', views.login, name='login'),

]
