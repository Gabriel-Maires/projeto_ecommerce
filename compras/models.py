from hmac import compare_digest
from itertools import product
from tabnanny import verbose
from django.db import models

# Create your models here.
class Shop(models.Model):
    cliente = models.CharField('cliente',max_lengh=100)
    create = models.DateField('criado em', auto_now_add=True, auto_now=False)
    
    class Meta:
        ordering=('-pk',)
        verbose_name='compra'
        verbose_name_plural='compras'
        
    def __str__(self):
        return self.cliente
    
class Product(models.Model):
    nome=models.CharField('nome',max_length=100,unique=True)   
    preco=models.DecimalField('preço',max_digits=6,decimal_places=2)
    
    class Meta:
        ordering=('name',)
        verbose_name='produto'
        verbose_name_plural='produtos'
        
    def __str__(self):
        return self.name
    
    def to_dict(self):
        return{
            'value':self.pk,
            'text':self.name,
            'preco':self.preco
        }
        
class Cart(models.Model):
    shop=models.ForeignKey(
        Shop,
        related_name='compras',
        on_delete=models.CASCADE
    )
    product=models.ForeignKey(
        Product,
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        
    )
    quantity=models.PositiveSmallIntegerField('quantidade')
    preco=models.DecimalField('preço',max_length=6,decimal_places=2)
    
    class Meta:
        ordering=('-pk',) 
        verbose_name='carrinho'
        verbose_name_plural='carrinhos'
        
    def __str__(self):
        if self.shop:
            return f'{self.shop.pk}-{self.pk}-{self.products}'
        return str(self.pk)
           
    def get_subtotal(self):
        return self.preco*(self.quantity or 0)