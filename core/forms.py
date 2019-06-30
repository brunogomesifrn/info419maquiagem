from django.forms import ModelForm
from .models import Tipo, Maquiagem

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']

class MaquiagemForm(ModelForm):
	class Meta(): 
		model = Maquiagem
		fields = ['nome', 'valor', 'descricao', 'tipos', 'foto']
	
