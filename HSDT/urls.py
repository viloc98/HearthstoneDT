from django.conf.urls import url
from django.urls import path, include


from . import views

app_name = "HSDT"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'cards/', views.cards, name='cards'),
    url(r'decks/', views.decks, name='decks'),
    url(r'deck_detail/', views.deck_detail, name='deck_detail'),
]
