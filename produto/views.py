from django.shortcuts import redirect, render

from .models import Categoria, Produto, Tamanho


# Create your views here.
def homepage(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    context = {"produto": produto, "categoria": categoria}
    return render(request, 'homepage.html', context)


def produto(request, id):
    if Produto.objects.filter(id=id):
        categoria = Categoria.objects.all()
        produto = Produto.objects.filter(id=id)
        context = {"produto": produto, "categoria": categoria}
        return render(request, 'produto.html', context)
    else:
        return redirect('/')


def cadastro_produtos(request):
    if request.method == "GET":
        tamanhos = Tamanho.objects.all()
        categoria = Categoria.objects.all()
        context = {"categorias": categoria, "tamanhos": tamanhos}
        return render(request, 'cadastro_produtos.html', context)
    elif request.method == "POST":
        nome = request.POST.get("nome")
        foto = request.POST.get("foto")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        importado = request.POST.get("importado")
        estoque_atual = request.POST.get("estoque_atual")
        estoque_min = request.POST.get("estoque_min")
        data = request.POST.get("data")
        categoria_form = request.POST.get("categoria")
        tamanho = request.POST.get("tamanho")
        
        produto_criar = Produto(nome=nome, foto=foto, descricao=descricao, preco=preco,
                                importado=importado, estoque_atual=estoque_atual, estoque_min=estoque_min,
                                data=data, categoria=Categoria.objects.get(nome=categoria_form), tamanho=Tamanho.objects.get(nome=tamanho))
        produto_criar.save()
        return redirect('/cadastro_produtos/')


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
    else:
        return redirect('/')
