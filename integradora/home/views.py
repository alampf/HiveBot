from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

@login_required
def home_view(request):
	return render(request, 'home.html')

def logout_view(request):
		logout(request)
		return redirect('login')

def login_view(request):
		if request.method == 'POST':
				username = request.POST['username']
				password = request.POST['password']
				user = authenticate(request, username=username, password=password)
				if user is not None:
						login(request, user)
						return redirect('home')
				else:
						return render(request, 'home/login.html', {'error': 'Credenciales incorrectas'})
		else:
				return render(request, 'home/login.html')

def logout_view(request):
		logout(request)
		return redirect('login')

def registro_view(request):
		if request.method == 'POST':
				form = UserCreationForm(request.POST)
				if form.is_valid():
						form.save()
						return redirect('login')
		else:
				form = UserCreationForm()
		return render(request, 'home/registro.html', {'form': form})


def home(request):
    return render(request, 'home/index.html')

def acerca(request):
    return render(request, 'home/acerca.html')

def asesoramiento(request):
    return render(request, 'home/asesoramiento.html')

def contacto(request):
    return render(request, 'home/contacto.html')