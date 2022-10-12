from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    foto = models.ImageField()
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=100000000)
    importado = models.BooleanField()
    estoque_atual = models.IntegerField()
    estoque_min = models.IntegerField()
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
