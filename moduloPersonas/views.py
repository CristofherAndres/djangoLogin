from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Usuario
from .forms import SignUpForm

@login_required
def personasIndex(request):
    """ Tarea:
     - Crear un dashboard para el admin
     - Crear un dashboard para el usuario
    """

    if request.user.is_superuser:
        return render(request, 'moduloPersonas/dashboardAdmin.html')
    if request.user.is_staff:
        return render(request, 'moduloPersonas/dashboardStaff.html')
    else:
        return render(request, 'moduloPersonas/dashboardUser.html')
    

def signUp(request):
    usuario = Usuario
    form = SignUpForm
    if request.method == 'POST':
        print("POST")
        form = SignUpForm(request.POST)
        """ Mostrar data del form """
        if form.is_valid():
            print("VALIDO")	
            form.save()
            return redirect('/')
        else:
            print("NO VALIDO")
            print(form.errors)	

    return render(request, 'moduloPersonas/signUp.html', {'form': form})


""" Agregar el formulario de panel sb2 """
""" Agregar los campos faltantes que agregamos al modelo Usuario """