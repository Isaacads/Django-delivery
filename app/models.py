from distutils.command.upload import upload
from tkinter.tix import Tree
from django.db import models



# Create your models here.
class Categoria(models.Model):
    tipo = models.CharField(max_length=150)

    def __str__(self):
        return self.tipo

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagem = models.ImageField()

    def __str__(self):
        return self.nome