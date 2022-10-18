from django.shortcuts import render
from .models import Produto
from .models import Cart


# Create your views here.
def produto_page(request):
    produto = Produto.objects.all()
    return render(request, 'produto_page.html', {"produto": produto})


#Gerenciamento do carrinho
def cart_home(request):
    cart_id=request.session.get('Cart_id',None)
    if cart_id is None:
        print('Create New Cart')
        request.session['cart_id']=123
    else:
        print('Cart ID exist')
    return render(request,'cart/home.html',{})
