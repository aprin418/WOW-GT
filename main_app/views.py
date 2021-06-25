from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

class Spec:
    def __init__(self, name, description):
        self.name = name
        self.description = description

Specs = [
    # Spec('Retibution', 'Standard ret spec'),
    # Spec('Protection', 'Prot paladin'),
]

def specs_index(request):
    return render(request, 'specs/index.html', {'specs': Specs})