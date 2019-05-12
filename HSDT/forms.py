from django.forms import ModelForm
from .models import *


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = '__all__'
