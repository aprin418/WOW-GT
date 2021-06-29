from django.shortcuts import render, redirect
from .models import Spec, Gear
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, request, response
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/specs')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/specs')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def profile(request, username):
    user = User.objects.get(username=username)
    specs = Spec.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'specs': specs})

def search(request):
    response=requests.get('https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&name.en_US=thunderfury&orderby=id&_page=1&access_token=US4jlqRC41Z9ovt3nPDj80fNGRMJoOZLOl')
    data = response.json()
    # print(data['results'])
    resultData = []
    for item in data['results']:
        print(item['data']['inventory_type']['name']['en_US'])
        gearDict = {
            'type': item['data']['inventory_type']['name']['en_US'],
            'name': item['data']['name']['en_US'],
        }
        resultData.append(gearDict)
        context = {'gearDict': resultData}
    print(resultData)
    print(context)
    return render(request, 'results.html', {'context': resultData})


def results(request):
    print("IN RESULTS")
    return render(request, 'results.html')

class SpecCreate(CreateView):
    model = Spec
    fields = ['name','description']

    def form_valid(self, form):
        print(self.__dict__)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        print(self.object)
        return HttpResponseRedirect('/specs/' + str(self.object.pk))

class SpecUpdate(UpdateView):
  model = Spec
  fields = ['name', 'description']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/specs/' + str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class SpecDelete(DeleteView):
  model = Spec
  success_url = '/specs'

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def specs_index(request):
    specs = Spec.objects.all()
    return render(request, 'specs/index.html', {'specs': specs})

def specs_show(request, spec_id):
        spec = Spec.objects.get(id=spec_id)
        return render(request, 'specs/show.html', {'spec': spec})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    specs = Spec.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'specs': specs})

def gear_index(request):
    gear = Gear.objects.all()
    return render(request, 'gear/index.html', {'gear': gear})

def gear_show(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    return render(request, 'gear/show.html', {'gear': gear})

class GearCreate(CreateView):
  model = Gear
  fields = "__all__"
  success_url = '/gear'

class GearUpdate(UpdateView):
    model = Gear
    fields = ['name', 'location']
    success_url = '/gear'

class GearDelete(DeleteView):
    model = Gear
    success_url = '/gear'