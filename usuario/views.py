from django.shortcuts import render
from django.views import View
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here.

def login(request):
    return render(request, 'usuario/login.html')

def registrar(request):
    return render(request, 'usuario/registrar.html')


@csrf_exempt
def crear(request):
    if request.method == 'POST':
        Usuario.objects.create(nombre=request.POST.get('nombre'), correo=request.POST.get('correo'), contraseña=request.POST.get('contraseña'), direccion=request.POST.get('direccion'), telefono=request.POST.get('telefono'), fecha_nacimiento=request.POST.get('fecha_nacimiento'))
    return render(request, 'usuario/login.html')
    #nombre=request.POST.get('nombre')
    #datos = {'message': nombre}
    #return JsonResponse(datos)

@csrf_exempt
def validar(request):
    if request.method == 'POST':
        nombre_v=request.POST.get('usuario')
        pass_v=request.POST.get('pass')
        usuario=list(Usuario.objects.filter(nombre=nombre_v).values())
        if len(usuario)>0:
            usuario=usuario[0]
            if (usuario["contraseña"]==pass_v):
                usuario=Usuario.objects.all() # select * from vehiculos
                data={'usuario':usuario}
                return render(request, 'usuario/lista.html',data)

            else:
                datos={'message': "pass incorresta..."}
            return JsonResponse(datos)
            
        else:
            datos={'message': "Usuarios not found..."}

        return JsonResponse(datos)

    else:
        datos = {'message': "a ocurrido un error"}
    
    return JsonResponse(datos)

def lista(request):
        usuario=Usuario.objects.all()
        data={'usuario':usuario}
        return render(request, 'usuario/lista.html',data)

def editar(request, id):
    usuario= list(Usuario.objects.filter(id=id).values())
    if len(usuario)>0:
        data={'usuario':usuario}
        return render(request, 'usuario/actualizar.html',data)

    else:
        datos={'message':"usuario not found..."} 
    return JsonResponse(datos)


@csrf_exempt
def modificar(request, id):
    usuario=list(Usuario.objects.filter(id=id).values())
    if len(usuario)>0:
        usuario=Usuario.objects.get(id=id)
        usuario.nombre=request.POST.get('nombre')
        usuario.correo=request.POST.get('correo')
        usuario.contraseña=request.POST.get('contraseña')
        usuario.direccion=request.POST.get('direccion')
        usuario.telefono=request.POST.get('telefono')
        usuario.fecha_nacimiento=request.POST.get('fecha_nacimiento')
        print(request.POST.get('fecha_nacimiento'))
        print("")
        usuario.save()
        usuario=Usuario.objects.all()
        data={'usuario':usuario}
        return render(request, 'usuario/lista.html',data)
    else:
        datos={'message':"usuario not found..."} 
    return JsonResponse(datos)

def eliminar(request, id):
    usuario= list(Usuario.objects.filter(id=id).values())
    if len(usuario)>0:
        Usuario.objects.filter(id=id).delete()
        usuario=Usuario.objects.all() # select * from vehiculos
        data={'usuario':usuario}
        return render(request, 'usuario/lista.html',data)

    else:
        datos={'message':"usuario not found..."} 
    return JsonResponse(datos)


class UsuarioView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def login(request):
        return render(request, 'usuario/login.html')
    
    def get(self, request, id=0):

        if(id>0):
            usuario=list(Usuario.objects.filter(id=id).values())
            if len(usuario)>0:
                usuario=usuario[0]
                datos={'message': "Success", 'usuario': usuario}
            else:
                datos={'message': "Usuarios not found..."}
            return JsonResponse(datos)
        else:
            usuario=list(Usuario.objects.values())
            if len(usuario) > 0:
                datos={'message':"Sucess", 'companies':usuario}
            else:
                datos={'message':"usuario not found..."}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Usuario.objects.create(nombre=jd['nombre'], correo=jd['correo'], contraseña=jd['contraseña'], direccion=jd['direccion'], telefono=jd['telefono'], fecha_nacimiento=jd['fecha_nacimiento'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        usuario=list(Usuario.objects.filter(id=id).values())
        if len(usuario)>0:
            usuario=Usuario.objects.get(id=id)
            usuario.nombre=jd['nombre']
            usuario.correo=jd['correo']
            usuario.contraseña=jd['contraseña']
            usuario.direccion=jd['direccion']
            usuario.telefono=jd['telefono']
            usuario.fecha_nacimiento=jd['fecha_nacimiento']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos={'message':"usuario not found..."} 
        return JsonResponse(datos)

    def delete(self, request, id):
        usuario= list(Usuario.objects.filter(id=id).values())
        if len(usuario)>0:
            Usuario.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos={'message':"usuario not found..."} 
        return JsonResponse(datos)