import requests
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'


@login_required(login_url='/HSDT/accounts/login')
def cards(request):
    url = 'https://omgvamp-hearthstone-v1.p.rapidapi.com/cards'
    headers = {"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com", "X-RapidAPI-Key": "39bec267c8mshd1a526c1f59a705p1a5cb3jsndf3b6d749365"}
    r = requests.get(url, headers=headers)
    json = r.json()
    print(json['Basic'])
    return render(request, 'cards.html', context=json)


@login_required(login_url='/HSDT/accounts/login')
def decks(request):
    return render(request, 'decks.html')
