from django.shortcuts import render
from .models import Produto
from django.shortcuts import redirect, render
from .models import Categoria, Produto


# Create your views here.
def homepage(request):
    produto = Produto.objects.all()
    return render(request, 'produto_page.html', {"produto": produto})


#Gerenciamento do carrinho
def cart_home(request):
    cart_id=request.session.get('Cart_id',None)
    if cart_id is None:
        print('Create New Cart')
        # precisa deixar dinamico
        request.session['cart_id']=123
    else:
        print('Cart ID exist')
        return render(request, 'cart/home.html', {})
      
    # precisa melhorar
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
