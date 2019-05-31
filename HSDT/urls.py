from django.conf.urls import url
from django.urls import path, include


from . import views

app_name = "HSDT"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'signup/', views.SignUp.as_view(), name='signup'),
    url(r'^cards/', views.cards, name='cards'),
    url(r'^decks/', views.decks, name='decks'),
    url(r'decks/', views.decks, name='decks'),
    url(r'deck_detail/(?P<pk>\w+)/', views.deck_detail, name='deck_detail'),
    url(r'^all_cards/', views.ViewCards.as_view(), name='all_cards'),
    url(r'^all_witchwood_cards/', views.ViewWitchwoodCards.as_view(), name='all_witchwood_cards'),
    url(r'^all_boomsday_cards/', views.ViewBoomsdayCards.as_view(), name='all_boomsday_cards'),
    url(r'^create_deck/', views.create_deck, name='create_deck'),
    url(r'^save_deck/', views.save_deck, name='save_deck'),
    url(r'^name/(?P<image>\w.+)(?P<clase>\d+)$', views.deck_name, name='deck_name'),
    url(r'^card_detail/(?P<pk>\w+)/', views.card_detail, name='card_detail'),
    url(r'search_teams/', views.teams, name='search_team'),
    url(r'my_team/(?P<user>\w*)/', views.my_teams, name='my_team'),
    url(r'team_profile/(?P<team>\d*)/', views.team_profile, name='team_profile'),

    url(r'^deck_detail/', views.deck_detail, name='deck_detail'),
    url(r'^deck_erase/(?P<pk>\w+)/', views.deck_erase, name='deck_erase'),
    url(r'^save_modifications/', views.save_modifications, name='save_modifications'),
    url(r'^deck_modify/(?P<pk>\w+)/', views.deck_modify, name='deck_modify'),

]
