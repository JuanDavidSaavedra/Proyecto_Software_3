from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from boletas.models import Compra
from .forms import NewUserForm

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context,request))

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('index')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context,request))

@login_required
def perfil_usuario(request):
    usuario = request.user
    reservas = Compra.objects.filter(usuario=usuario)
    return render(request, 'perfil.html', {
        'usuario': usuario,
        'reservas': reservas
    })