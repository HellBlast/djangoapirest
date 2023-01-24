from django.urls import path
from .views import UsuarioView
from . import views

urlpatterns = [
    path('', UsuarioView.as_view(), name='login_list'),
    path('<int:id>', UsuarioView.as_view(), name='login_process'),
    path('login',views.login, name='login'),
    path('registrar',views.registrar, name='registrar'),
    path('crear/',views.crear, name='crear'),
    path('validar/',views.validar, name='validar'),
    path('lista',views.lista, name='lista'),
    path('editar/<int:id>/',views.editar, name='editar'),
    path('eliminar/<int:id>/',views.eliminar, name='eliminar'),
    path('modificar/<int:id>',views.modificar, name='modificar'),
    #path('actualizar/<id>/',views.actualizar, name='actualizar'),
]