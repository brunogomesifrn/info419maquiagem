from django.db import models


class Tipo(models.Model):
	nome = models.CharField('Nome', max_length=150)
class Maquiagem(models.Model):
	nome = models.CharField('Nome', max_length=150)	
	valor = models.DecimalField('Valor', max_digits=4, decimal_places=2)
	Descricao = models.CharField('Descrição', max_length=300)
	tipos =  models.ForeignKey(Tipo, on_delete=models.CASCADE)


# Create your models here.
