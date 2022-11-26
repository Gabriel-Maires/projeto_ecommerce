from django.db import models
from produto.models import Produto
from datetime import datetime

# Create your models here.
class Vendendor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Vendas(models.Model):
    vendendor = models.ForeignKey(Vendendor, on_delete=models.DO_NOTHING, blank=True, null=True) 
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, blank=True)
    despesas = models.FloatField()
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.produto.nome


