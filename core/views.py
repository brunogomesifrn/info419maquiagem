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
	lista = Maquiagem.objects.all()

	contexto = {
	'lista_Maquiagem': lista
	}
	return render(request, 'usuario.html', contexto)

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

def tipo (request):
	lista = Tipo.objects.all()

	contexto = {
	'lista_Tipo': lista
	}
	return render(request, 'tipo.html', contexto)

def Cadastrartipo (request):
	form = TipoForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('tipo')
	
	contexto = {
	'form': form
	}
	return render(request, 'Cadastrartipo.html', contexto)

def editartipo(request, id):
	tipo = Tipo.objects.get(pk=id)
	form = TipoForm(request.POST or None, instance=tipo)

	if form.is_valid():
		form.save()
		return redirect('tipo')

	contexto = {
	'form': form
	}

	return render(request, 'Cadastrartipo.html', contexto)

def excluirtipo(request, id):
	tipo = Tipo.objects.get(pk=id)
	tipo.delete()
	
	return redirect('tipo')


def editar(request, id):
	lista = Maquiagem.objects.get(pk=id)
	form = MaquiagemForm(request.POST or None, request.FILES or None, instance=lista)

	if form.is_valid():
		form.save()
		return redirect('usuario')

	contexto = {
	'form': form
	}

	return render(request, 'add.html', contexto)

def excluir(request, id):
	lista = Maquiagem.objects.get(pk=id)
	Maquiagem.delete()
	
	return redirect('usuario')

