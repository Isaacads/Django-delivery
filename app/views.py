from django.shortcuts import render

from app.models import Produto

# Create your views here.

def home (request):
    produtos = Produto.objects.all()
    return render(request, 'index.html',{'produtos':produtos})