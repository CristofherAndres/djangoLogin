from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

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