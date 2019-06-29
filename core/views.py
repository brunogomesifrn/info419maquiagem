from django.shortcuts import render, redirect

# Create your views here.

def pagina(request):
	return render(request, 'pagina_inicial.html')

def cadastro(request):
	return render(request, 'cadastro.html')

def login(request):
	return render(request, 'login.html')

def usuario(request):
	return render(request, 'usuario.html')

def adicionar(request):
	return render(request, 'add.html')


