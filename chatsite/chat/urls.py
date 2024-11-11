from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a página inicial do chat
    path('news/', views.news, name='news'),
]