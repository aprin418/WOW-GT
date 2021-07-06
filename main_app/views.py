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
import json


def login_view(request):
    # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/specs/')
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else:  # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


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


@login_required
def search(request):
    response = requests.get(
        'https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&name.en_US=power&orderby=id&_page=1&access_token=USOu9OOJYc5FZCZUOiYmPrcOydkWwSaAEd')
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


@login_required
def results(request):
    print("IN RESULTS")
    return render(request, 'results.html')


class SpecCreate(CreateView):
    model = Spec
    fields = ['character', 'name', 'description']

    def form_valid(self, form):
        print(self.__dict__)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        print(self.object)
        return HttpResponseRedirect('/specs/' + str(self.object.pk))


class SpecUpdate(UpdateView):
    model = Spec
    fields = ['character', 'name', 'description']

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


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def specs_index(request):
    # specs = Spec.objects.all()
    specs = Spec.objects.filter(user_id=request.user.id)
    print(specs)
    return render(request, 'specs/index.html', {'specs': specs})


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    # specs = Spec.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username})


@login_required
def gear_index(request):
    gear = Gear.objects.all()
    return render(request, 'gear/index.html', {'gear': gear})


@login_required
def gear_show(request, gear_id):
    # gear = Gear.objects.get(id=gear_id)
    gear = Gear.objects.get(pk=gear_id)
    return render(request, 'gear/show.html', {'gear': gear})


class GearUpdate(UpdateView):
    model = Gear
    fields = ['name', 'slot', 'location', 'enchant']
    # success_url = '/specs'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/gear/' + str(self.object.pk))


class GearDelete(DeleteView):
    model = Gear
    success_url = '/specs'


def parse_data(data):
    product = {}
    if 'csrfmiddlewaretoken' in data[0]:
        product['csrfmiddlewaretoken'] = data[0].split('=')[1]
        data.pop(0)
    #     print('( new data )', data)
    # print('( woah MULE )')
    for item in data:
        # print('( item )', item)
        # new_phrase = None
        if '+' in item:
            new_key = item.split('=')[0]
            words = item.split('=')[1].split('+')
            new_words = (' ').join(words)
            # print('( final phase )', new_words)
            product[new_key] = new_words
        else:
            new_key = item.split('=')[0]
            new_value = item.split('=')[1]
            product[new_key] = new_value

    return product


@login_required
def specs_show(request, spec_id):
    spec = Spec.objects.get(id=spec_id)
    gear = Gear.objects.filter(spec=spec_id)
    data = {
        'spec': spec,
        'gear': gear
    }
    return render(request, 'specs/show.html', data)


@login_required
def gear_create(request, spec_id):
    spec = Spec.objects.get(id=spec_id)
    user = request.user

    return render(request, 'gear.html', {'spec': spec, 'user': user})


def assoc_spec_gear(request):
    split_form_data = request.body.decode('utf-8').split('&')
    # print(type(request.body))
    # print(split_form_data)
    # print('spec split form data', split_form_data)
    x = parse_data(split_form_data)
    # print('( x )', x)
    print(request.user.id)
    # new_age = int(x.get('age'))
    # x['age']= new_age
    # new_spec = int(x.get('spec').split("'")[0]) # 1
    # x['spec'] = new_spec

    print('( NEW X )', x)
    g = Gear(
        name=x.get('name'),
        slot=x.get('slot'),
        location=x.get('location'),
        enchant=x.get('enchant'),
        user_id=request.user.id,
        spec_id=int(x.get('spec_id'))
    )
    g.save()

    print('( NEW Gear )', g)

    print('( proof )', Gear.objects.get(id=g.id))

    return HttpResponseRedirect('/specs')
