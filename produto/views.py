from django.shortcuts import render

from .models import Categoria, Produto


# Create your views here.
def homepage(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    context = {"produto": produto, "categoria": categoria}
    return render(request, 'homepage.html', context)


def categorias(request):
    categoria = Categoria.objects.all()
    context = {"categorias": categoria}
    return render(request, 'categorias.html', context)


def collectionsview(request, nome):
    if Categoria.objects.filter(nome=nome):
        produtos = Produto.objects.filter(nome=nome)
        nome_categoria = Categoria.objects.filter(nome=nome).first()
        context = {"produtos": produtos, "nome_categoria": nome_categoria}
        return render(request, 'collections.html', context)
