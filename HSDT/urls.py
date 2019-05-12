from django.conf.urls import url
from django.urls import path, include


from . import views

app_name = "HSDT"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'signup/', views.SignUp.as_view(), name='signup'),
    url(r'^cards/', views.cards, name='cards'),
    url(r'decks/', views.decks, name='decks'),
    url(r'^all_cards/', views.ViewCards.as_view(), name='all_cards'),
    url(r'^all_witchwood_cards/', views.ViewWitchwoodCards.as_view(), name='all_witchwood_cards'),
    url(r'^all_boomsday_cards/', views.ViewBoomsdayCards.as_view(), name='all_boomsday_cards'),

    url(r'deck_detail/', views.deck_detail, name='deck_detail'),
]
