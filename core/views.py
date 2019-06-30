from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'cadastro.html', contexto)

def usuario(request):
	return render(request, 'usuario.html')

def adicionar(request):
	return render(request, 'add.html')

