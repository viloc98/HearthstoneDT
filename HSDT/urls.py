from django.conf.urls import url
from . import views

app_name = "HSDT"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'cards/', views.cards, name='cards'),
    url(r'decks/', views.decks, name='decks'),

]