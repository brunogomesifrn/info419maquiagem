from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Maquiagem, Tipo
from .forms import  MaquiagemForm, TipoForm

#from django.contrib.auth.models import User
# Create your views here.

def pagina(request):
	return render(request, 'pagina_inicial.html')

@login_required
def usuario(request):
		return render(request, 'usuario.html')

def cadastro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('usuario')
	contexto = {
		'form': form
	}
	return render(request, 'cadastro.html', contexto)

def adicionar(request):
	form = MaquiagemForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		form.save()
		return redirect('usuario')
	
	contexto = {
	'form': form
	}
	return render(request, 'add.html', contexto)

def editar(request, id):
	Maquiagem = Maquiagem.objects.get(pk=id)
	form = MaquiagemForm(request.POST or None, request.FILES or None, instance=Maquiagem)

	if form.is_valid():
		form.save()
		return redirect('usuario')

	contexto = {
	'form': form
	}

	return render(request, 'usuario.html', contexto)

def excluir(request, id):
	Maquiagem = Maquiagem.objects.get(pk=id)
	Maquiagem.delete()
	
	return redirect('usuario')

