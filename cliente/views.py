from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from eventos.models import Certificado
# Create your views here.

@login_required
def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})
