from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Proyecto
from django.http import JsonResponse
from .forms import FormularioProyecto

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def group_required(*group_names):

    def check(user):
        if user.groups.filter(name__in=group_names).exists()    | user.is_superuser:
            return True
        else:
            return False
    return user_passes_test(check, login_url='incorrect_user/')


@login_required
@group_required('Estudiante')
def crear(request):
    if(request.POST):
        #capturar datos desde el formulario
        nombre = request.POST["txtNombre"]
        estudiante = request.POST['txtEstudiante']
        email = request.POST['txtEmail']
        tema = request.POST['cboTema']
        descripcion = request.POST['txtDescripcion']
        profesor = ''
        #validaciones de reglas de negocio

        #construir y cargar el objeto con los datos del form
        proyecto = Proyecto()
        proyecto.nombre = nombre
        proyecto.estudiante = estudiante
        proyecto.email = email
        proyecto.tema = tema
        proyecto.descripcion = descripcion
        proyecto.profesor = profesor

        #guardar cambios en la base de datos
        proyecto.save()
    return render(request, 'core/crear.html')

@login_required
@group_required('Profesor')
def ver(request):
    return render(request, 'core/ver.html')

def exit(request):
    logout(request)
    return redirect('home')

@login_required
@group_required('Profesor')
def mostrar_proyectos(request):
    tiene_profesor = request.GET.get('tiene_profesor')
    if tiene_profesor == 'asignado':
        proyectos = Proyecto.objects.exclude(profesor__isnull=True).exclude(profesor__exact='')
    elif tiene_profesor == 'no_asignado':
        proyectos = Proyecto.objects.filter(profesor__isnull=True) | Proyecto.objects.filter(profesor__exact='')
    else:
        proyectos = Proyecto.objects.all()
    return render(request, 'core/ver.html', {'proyectos': proyectos, 'tiene_profesor': tiene_profesor})

@login_required
def asignar_profesor(request, proyecto_id):
    if request.method == 'POST':
        proyecto = get_object_or_404(Proyecto, id=proyecto_id)
        if not proyecto.profesor:
            proyecto.profesor = request.user.username
            proyecto.save()
            return JsonResponse({'success': True, 'profesor': proyecto.profesor})
    return JsonResponse({'success': False})


def proyectos_con_profesor(request):
    tema = request.GET.get('tema')
    if tema:
        proyectos = Proyecto.objects.exclude(profesor__isnull=True).exclude(profesor__exact='').filter(tema=tema)
    else:
        proyectos = Proyecto.objects.exclude(profesor__isnull=True).exclude(profesor__exact='')
    return render(request, 'core/home.html', {'proyectos': proyectos, 'tema': tema})



@login_required
@group_required('Estudiante')
def proyectos_estudiante(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'core/lista_estudiante.html', {'proyectos': proyectos})

@login_required
@group_required('Estudiante')
def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == 'POST':
        form = FormularioProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos_estudiante')
    else:
        form = FormularioProyecto(instance=proyecto)
    return render(request, 'core/editar.html', {'form': form, 'proyecto': proyecto})