from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def acesso(request):
    if cadastrado == true:
        return render(request, 'home.html')
    else:
        return render(request, 'cadastrar.html')