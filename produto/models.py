from email.policy import default
from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    foto = models.ImageField()
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=100000000)
    importado = models.BooleanField(default=False)
    estoque_atual = models.IntegerField()
    estoque_min = models.IntegerField()
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    avaliacao = models.IntegerField(blank=True)

    def __str__(self):
        return self.nome
    


   
 
