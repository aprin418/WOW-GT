from django.shortcuts import render
from django.http import HttpResponse
from .models import Spec

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

class Spec:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def specs_index(request):
    specs = Spec.objects.all()
    return render(request, 'specs/index.html', {'specs': specs})