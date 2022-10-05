from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """registrar un nuevo usuario"""  
    if request.method != 'POST':
        # muestra forma de registro en blanco
        form = UserCreationForm()
    else:
        # procesar forma completada.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # accesando en usuario dentro y redirigir al home page
            login(request, new_user)
            return redirect('Aprendo:index')
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_request(request): #agregado 3/10/22
    return redirect(request,'users:logout')
    