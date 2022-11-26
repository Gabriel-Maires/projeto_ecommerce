from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('retorna_total_vendido/', views.retorna_total_vendido, name="retorna_total_vendido"),
    path('relatorio_faturamento/', views.relatorio_faturamento, name="relatorio_faturamento"),
    path('relatorio_produto/', views.relatorio_produto, name="relatorio_produto"),
]