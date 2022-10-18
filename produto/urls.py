from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<str:nome>', views.collectionsview, name='collectionsview')
]
