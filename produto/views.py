from django.shortcuts import render

from .models import Produto


# Create your views here.
def produto_page(request):
    produto = Produto.objects.all()
    return render(request, 'produto_page.html', {"produto": produto})
