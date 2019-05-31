import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from HSDT import forms
from HSDT.forms import DeckForm
from HSDT.models import *


def index(request):
    return render(request, 'index.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'


@login_required(login_url='/HSDT/accounts/login')
def cards(request):
    cards = Card.objects.all()
    if not cards:
        url = 'https://omgvamp-hearthstone-v1.p.rapidapi.com/cards'
        headers = {"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com",
                   "X-RapidAPI-Key": "39bec267c8mshd1a526c1f59a705p1a5cb3jsndf3b6d749365"}
        r = requests.get(url, headers=headers)
        json = r.json()
        keys = json.keys()
        for key in keys:
            for current_card in json[key]:
                if 'cardId' in current_card and 'name' in current_card and 'cardSet' in current_card and 'type' in current_card and 'rarity' in current_card and 'cost' in current_card and 'playerClass' in current_card and 'img' in current_card:
                    if 'attack' in current_card and 'health' in current_card and 'race':
                        newCard = Card(cardID=current_card['cardId'], name=current_card['name'],
                                       cardSet=current_card['cardSet'], type=current_card['type'],
                                       rarity=current_card['rarity'], cost=current_card['cost'],
                                       attack=current_card['attack'], health=current_card['health'],
                                       text="", race="",
                                       playerClass=current_card['playerClass'], img=current_card['img'])
                        newCard.save()
                    else:
                        newCard = Card(cardID=current_card['cardId'], name=current_card['name'],
                                       cardSet=current_card['cardSet'], type=current_card['type'],
                                       rarity=current_card['rarity'], cost=current_card['cost'],
                                       attack=None, health=None,
                                       text="", race="",
                                       playerClass=current_card['playerClass'], img=current_card['img'])
                        newCard.save()

    return render(request, 'cards.html')


@login_required(login_url='/HSDT/accounts/login')
def decks(request):
    # getting our template
    template = loader.get_template('decks.html')

    decks = Deck.objects.filter(author=request.user)
    context = {'decks': decks}

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context))


class ViewCards(ListView):
    template_name = 'all_cards.html'
    model = Card
    context_object_name = "cards"

    def get_context_data(self, **kwargs):
        context = super(ViewCards, self).get_context_data(**kwargs)
        context['title'] = 'All cards'
        context['druid'] = Card.objects.all().filter(playerClass__exact="Druid").order_by('cost')
        context['hunter'] = Card.objects.all().filter(playerClass__exact="Hunter").order_by('cost')
        context['mage'] = Card.objects.all().filter(playerClass__exact="Mage").order_by('cost')
        context['priest'] = Card.objects.all().filter(playerClass__exact="Priest").order_by('cost')
        context['paladin'] = Card.objects.all().filter(playerClass__exact="Paladin").order_by('cost')
        context['rogue'] = Card.objects.all().filter(playerClass__exact="Rogue").order_by('cost')
        context['shaman'] = Card.objects.all().filter(playerClass__exact="Shaman").order_by('cost')
        context['warlock'] = Card.objects.all().filter(playerClass__exact="Warlock").order_by('cost')
        context['warrior'] = Card.objects.all().filter(playerClass__exact="Warrior").order_by('cost')
        context['neutral'] = Card.objects.all().filter(playerClass__exact="Neutral").order_by('cost')

        return context

    def get_queryset(self):
        return super(ViewCards, self).get_queryset()


def card_detail(request, pk):
    card = {}
    card['card'] = Card.objects.filter(cardID=pk)
    return render(request, 'card_detail.html', context=card)


class ViewWitchwoodCards(ListView):
    template_name = 'all_cards.html'
    model = Card
    context_object_name = "cards"

    def get_context_data(self, **kwargs):
        context = super(ViewWitchwoodCards, self).get_context_data(**kwargs)
        context['title'] = 'The Witchwood'
        context['druid'] = Card.objects.all().filter(playerClass__exact="Druid",
                                                     cardSet__exact="The Witchwood").order_by('cost')
        context['hunter'] = Card.objects.all().filter(playerClass__exact="Hunter",
                                                      cardSet__exact="The Witchwood").order_by('cost')
        context['mage'] = Card.objects.all().filter(playerClass__exact="Mage", cardSet__exact="The Witchwood").order_by(
            'cost')
        context['priest'] = Card.objects.all().filter(playerClass__exact="Priest",
                                                      cardSet__exact="The Witchwood").order_by('cost')
        context['paladin'] = Card.objects.all().filter(playerClass__exact="Paladin",
                                                       cardSet__exact="The Witchwood").order_by('cost')
        context['rogue'] = Card.objects.all().filter(playerClass__exact="Rogue",
                                                     cardSet__exact="The Witchwood").order_by('cost')
        context['shaman'] = Card.objects.all().filter(playerClass__exact="Shaman",
                                                      cardSet__exact="The Witchwood").order_by('cost')
        context['warlock'] = Card.objects.all().filter(playerClass__exact="Warlock",
                                                       cardSet__exact="The Witchwood").order_by('cost')
        context['warrior'] = Card.objects.all().filter(playerClass__exact="Warrior",
                                                       cardSet__exact="The Witchwood").order_by('cost')
        context['neutral'] = Card.objects.all().filter(playerClass__exact="Neutral",
                                                       cardSet__exact="The Witchwood").order_by('cost')
        return context

    def get_queryset(self):
        return super(ViewWitchwoodCards, self).get_queryset()


class ViewBoomsdayCards(ListView):
    template_name = 'all_cards.html'
    model = Card
    context_object_name = "cards"

    def get_context_data(self, **kwargs):
        context = super(ViewBoomsdayCards, self).get_context_data(**kwargs)
        context['title'] = 'The Boomsday Project'
        context['druid'] = Card.objects.all().filter(playerClass__exact="Druid",
                                                     cardSet__exact="The Boomsday Project").order_by('cost')
        context['hunter'] = Card.objects.all().filter(playerClass__exact="Hunter",
                                                      cardSet__exact="The Boomsday Project").order_by('cost')
        context['mage'] = Card.objects.all().filter(playerClass__exact="Mage",
                                                    cardSet__exact="The Boomsday Project").order_by('cost')
        context['priest'] = Card.objects.all().filter(playerClass__exact="Priest",
                                                      cardSet__exact="The Boomsday Project").order_by('cost')
        context['paladin'] = Card.objects.all().filter(playerClass__exact="Paladin",
                                                       cardSet__exact="The Boomsday Project").order_by('cost')
        context['rogue'] = Card.objects.all().filter(playerClass__exact="Rogue",
                                                     cardSet__exact="The Boomsday Project").order_by('cost')
        context['shaman'] = Card.objects.all().filter(playerClass__exact="Shaman",
                                                      cardSet__exact="The Boomsday Project").order_by('cost')
        context['warlock'] = Card.objects.all().filter(playerClass__exact="Warlock",
                                                       cardSet__exact="The Boomsday Project").order_by('cost')
        context['warrior'] = Card.objects.all().filter(playerClass__exact="Warrior",
                                                       cardSet__exact="The Boomsday Project").order_by('cost')
        context['neutral'] = Card.objects.all().filter(playerClass__exact="Neutral",
                                                       cardSet__exact="The Boomsday Project").order_by('cost')
        return context

    def get_queryset(self):
        return super(ViewBoomsdayCards, self).get_queryset()


@login_required(login_url='/HSDT/accounts/login')
def deck_detail(request, pk):
    deck_data = Deck.objects.get(id=pk)
    crds = Card.objects.filter(cardindeck__deck=pk).order_by('cost', 'name')
    return render(request, 'deck_detail.html', {'deck_name': deck_data.name, 'deck_description': deck_data.description,
                                                'deck_image': deck_data.image, 'cards': crds})


@login_required(login_url='/HSDT/accounts/login')
def deck_erase(request, pk):
    deck_data = Deck.objects.get(id=pk).delete()
    return redirect('HSDT:decks')


@login_required(login_url='/HSDT/accounts/login')
def deck_modify(request, pk):
    deck_data = Deck.objects.get(id=pk)
    data = {'name': deck_data.name, 'image': deck_data.image, 'description': deck_data.description,
            'playerClass': deck_data.playerClass}
    form = DeckForm(initial=data)

    return render(request, "deck_modify_form.html", {'form': form})


def save_modifications(request, pk):
    form = DeckForm(request.POST)
    if form.is_valid():
        model_instance = form.save(commit=False)
        model_instance.save()
        return redirect('HSDT:decks')


@login_required(login_url='/HSDT/accounts/login')
def create_deck(request):
    return render(request, 'create_deck.html')


def deck_name(request, image, clase):
    data = {'image': image, 'playerClass': clase, 'author': request.user}
    cards = Card.objects.filter
    form = DeckForm(initial=data)
    return render(request, "deck_form.html", {'form': form})


def save_deck(request):
    form = DeckForm(request.POST)
    if form.is_valid():
        model_instance = form.save(commit=False)
        model_instance.save()
        deck_name = model_instance.pk
        deck = Deck.objects.get(pk=deck_name)
        return render(request, 'cards_in_deck.html', {'deck': deck})


@login_required(login_url='/HSDT/accounts/login')
def teams(request):
    team = {}
    search = request.GET.get('q')
    if search:
        query = Team.objects.filter(name__contains=search)
    else:
        query = Team.objects.filter(name__contains="")
    if query:
        team['query'] = query
    return render(request, 'search_team.html', context=team)


@login_required(login_url='/HSDT/accounts/login')
def my_teams(request):
    team = {}
    search = request.GET.get('q')
    if search:
        query = Team.objects.filter(playerinteam__user=request.user, name__contains=search)
    else:
        query = Team.objects.filter(playerinteam__user=request.user, name__contains="")
    if query:
        team['query'] = query
    return render(request, 'my_teams.html', context=team)


@login_required(login_url='/HSDT/accounts/login')
def team_profile(request, team, user):
    team_to_show = {}
    query = Team.objects.filter(pk=team)
    players_query = PlayerInTeam.objects.filter(team=Team.objects.get(pk=team), user=User.objects.get(pk=user))
    team_to_show['query'] = query
    if players_query:
        team_to_show['players_query'] = players_query

    return render(request, 'team_profile.html', context=team_to_show)


@login_required(login_url='/HSDT/accounts/login')
def leave_team(request, user, team):
    if PlayerInTeam.objects.filter(user=User.objects.get(pk=user), team=Team.objects.get(pk=team)):
        PlayerInTeam.delete(
            PlayerInTeam.objects.get(user=User.objects.get(pk=user), team=Team.objects.get(pk=team)))
    return team_profile(request, user, team)


@login_required(login_url='/HSDT/accounts/login')
def join_team(request, user, team):
    if not PlayerInTeam.objects.filter(team=Team.objects.get(id=team), user=User.objects.get(id=user)):
        player_in_team = PlayerInTeam(team=Team.objects.get(id=team), user=User.objects.get(id=user))
        player_in_team.save()
    return team_profile(request, user, team)


def team_decks(request, team):
    print("hey")
    users = PlayerInTeam.objects.filter(team__playerinteam__team_id=team)
    for user in users:
        print("hey")
        print(user.user)
    decks = list()
    for player in users:
        decks.__add__(Deck.objects.filter(author=player.pk))
    print(decks[1])
    context = {'decks': decks}
    return render(request, 'decks.html', context=context)
