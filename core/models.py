from django.db import models

#class Login(models.Model):
	#email = EmailField(max_length=30)-->

class Tipo(models.Model):
	nome = models.CharField('Nome', max_length=150)

	def __str__(self):
		return self.nome

class Maquiagem(models.Model):
	nome = models.CharField('Nome', max_length=150)	
	valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
	descricao = models.CharField('Descrição', max_length=300)
	tipos =  models.ForeignKey(Tipo, on_delete=models.CASCADE)
	foto= models.ImageField('Foto', upload_to="fotos", null=True)




