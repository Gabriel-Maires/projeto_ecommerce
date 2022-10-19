from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.contrib.auth.models import User


class Usuario(AbstractUser):
  
    sobrenome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11) 
    cep = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(null=True)
    numero = models.CharField(max_length=20)




    def __str__(self):
        return self.username
 




class Token(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    validade = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username



class Token_login(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    login_codigo = models.CharField(max_length=200)