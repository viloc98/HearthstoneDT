from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def cards(request):
    return render(request, 'cards.html')


def decks(request):
    return render(request, 'decks.html')