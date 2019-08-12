from django.shortcuts import render
from .models import Ajudado, Ajudante


# Create your views here.
global telefone

def render_index(request):
    return render(request, 'index.html')

def acesso(request):
    ajudado_bd = Ajudado.objects.filter(telefone=request.GET.get('telefone')).first()
    telefone = request.GET.get('telefone')
    if ajudado_bd is not None:
        return render(request, 'home.html', {'ajudado': ajudado_bd})
    else:
        return render(request, 'cadastrar.html', {'telefone': telefone})
        

def render_cadastro(request):
    ajudado = Ajudado()
    if request.method == 'POST':
        ajudado.telefone = request.POST.get('telefone')
        ajudado.nome = request.POST.get('nome')
        ajudado.sobrenome = request.POST.get('sobrenome')
        ajudado.email = request.POST.get('email')
        ajudado.save()
        return render(request, 'home.html')
    return render(request, 'cadastrar.html')

def render_home(request):
    return render(request, 'home.html')