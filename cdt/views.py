from django.shortcuts import render , get_object_or_404
from . import models


def index(request):
    pessoas = models.Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas':pessoas},)

def pessoa(request, id):
    pessoa = get_object_or_404(models.Pessoa, id=id)
    return render(request, 'pessoa.html', {'pessoa':pessoa})

# Create your views here.
