from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request, 'cards.html')


@login_required(login_url='/HSDT/accounts/login')
def decks(request):
    return render(request, 'decks.html')
