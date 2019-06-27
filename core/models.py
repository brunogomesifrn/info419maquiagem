from django.db import models


class Tipo(models.Model):
	nome = models.Charfield('Nome', max_lenght=150)
class Maquiagem(models.Model):
	nome = models.Charfield('Nome', max_lenght=150)	
	valor = models.Decimalfield('Valor', max_digits=4, decimal_places=2)
	Descricao = model.Charfield('Descrição', max_lenght=300)


# Create your models here.
