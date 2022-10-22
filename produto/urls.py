from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('produtos/<str:id>', views.produto, name='produto'),
    path('cadastro_produtos/', views.cadastro_produtos, name='cadastro_produtos'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<str:nome>', views.collectionsview, name='collectionsview'),
    path('avaliacao/<str:id>', views.avaliacao, name='avaliacao')
]
