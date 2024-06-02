"""
URL configuration for C2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home, crear, ver, exit, mostrar_proyectos, asignar_profesor, proyectos_con_profesor, proyectos_estudiante, editar_proyecto

urlpatterns = [
    path('', proyectos_con_profesor, name="home"),
    path('crear/', crear, name="crear"),
    path('ver/', mostrar_proyectos, name="ver"),
    path('logout/', exit, name="exit"),
    path('crear/incorrect_user/', exit, name="incorrect_user_crear"),
    path('ver/incorrect_user/', exit, name="incorrect_user_ver"),
    path('asignar/<int:proyecto_id>/', asignar_profesor, name="asignar_profesor"),
    path('home/', proyectos_con_profesor, name="proyectos_con_profesor"),
    path('estudiante/', proyectos_estudiante, name="proyectos_estudiante"),
    path('editar/<int:proyecto_id>/', editar_proyecto, name="editar_proyecto"),
]