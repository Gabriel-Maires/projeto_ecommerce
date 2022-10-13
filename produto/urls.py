from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.produto_page, name="produto_page"),
]