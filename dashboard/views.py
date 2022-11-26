from django.shortcuts import render, HttpResponse
from django.db.models import Sum
from django.http import JsonResponse
from .models import Vendas, Vendendor
from produto.models import Produto
from datetime import datetime
from django.core import serializers
import json

def home(request):
    return render(request, 'dashboard.html')

def retorna_total_vendido(request):
    faturamento_total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    despesas_totais =  Vendas.objects.all().aggregate(Sum('despesas'))['despesas__sum']
    lucro_total = faturamento_total - despesas_totais
    
    return JsonResponse({'data':lucro_total})

def relatorio_faturamento(request):
    vendas = Vendas.objects.all()

    meses = ['jan', 'feb', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    despesas = []
    lucro = []
    mes = datetime.now().month + 1
    ano = datetime.now().year

    for i in range(12):

        mes -= 1

        if mes == 0:
            mes = 12
            ano -= 1

        soma_do_mes = sum([i.total for i in vendas if i.data.month == mes and i.data.year == ano])
        despesas_do_mes = sum([i.despesas for i in vendas if i.data.month == mes and i.data.year == ano])
        lucro_do_mes = soma_do_mes - despesas_do_mes

        despesas.append(despesas_do_mes)
        data.append(soma_do_mes)
        labels.append(meses[mes-1])
        lucro.append(lucro_do_mes)


    data_json = {'data': data[::-1], 'labels': labels[::-1], 'data_despesas':despesas[::-1], 'lucro':lucro[::-1]}

    return JsonResponse(data_json)

def relatorio_produto(request):

    produtos = Produto.objects.all()

    data = []
    labels = []

    for produto in produtos:
        valor_total = Vendas.objects.filter(produto=produto).aggregate(Sum('total'))['total__sum']

        if not valor_total:
            valor_total = 0

        labels.append(produto.nome)
        data.append(valor_total)

    aux = list(zip(labels, data))

    aux.sort(key= lambda x: x[1], reverse=True)

    aux = list(zip(*aux))

    data = aux[1][0:5]
    labels = aux[0][0:5]

    return JsonResponse({'data':data, 'labels':labels})
