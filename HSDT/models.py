from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CLASSES = ((0, "Druid"), (1, "Hunter"), (2, "Mage"), (3, "Paladin"), (4, "Priest"), (5, "Rogue"), (6, "Shaman"), (7, "Warlock"), (8, "Warrior"), (9, "Dream"), (10, "Neutral"), (None, ''))

SETS = ((0, "Basic"), (1, "Classic"), (2, "Promo"), (3, "Hall of Fame"), (4, "Naxxramas"), (5, "Goblins vs Gnomes"), (6, "Blackrock Mountain"), (7, "The Grand Tournament"),
        (8, "The League of Explorers"), (9, "Whispers of the Old Gods"), (10, "One Night in Karazhan"), (11, "Mean Streets of Gadgetzan"), (12, "Journey to Un'Goro"),
        (13, "Knights of the Frozen Throne"), (14, "Kobolds & Catacombs"), (15, "The Witchwood"), (16, "The Boomsday Project"), (17, "Rastakhan's Rumble"), (18, "Rise of Shadows"),
        (19,"Tavern Brawl"), (20, "Taverns of Time"), (21, "Hero Skins"), (22, "Missions"), (23, "Credits"), (24, "System"), (25, "Debug"),)

TYPES = ((0, "Hero"), (1, "Minion"), (2, "Spell"), (3, "Enchantment"), (4, "Weapon"), (5, "Hero Power"),)

QUALITIES = ((0, "Free"), (1, "Common"), (2, "Rare"), (3, "Epic"), (4, "Legendary"),)

RACES = ((0, "Demon"), (1, "Dragon"), (2, "Elemental"), (3, "Mech"), (4, "Murloc"), (5, "Beast"), (6, "Pirate"), (7, "Totem"),)


class Card(models.Model):
    cardID = models.CharField("Card ID", max_length=8, primary_key=True)
    name = models.CharField("Name", max_length=30)
    cardSet = models.CharField("Card Set", max_length=100, choices=SETS)
    type = models.CharField("Type", max_length=30, choices=TYPES)
    rarity = models.CharField("Rarity", max_length=30, choices=QUALITIES)
    cost = models.IntegerField("Cost")
    attack = models.IntegerField("Attack", null=True)
    health = models.IntegerField("Health", null=True)
    text = models.TextField("Text", default="")
    race = models.CharField("Race", max_length=30, choices=RACES)
    playerClass = models.CharField("Player Class", max_length=30, choices=CLASSES)
    img = models.URLField("Image")

    def __str__(self):
        return self.name


class Deck(models.Model):
    name = models.CharField("Name", max_length=200)
    description = models.CharField("Description", max_length=2000, default="")
    playerClass = models.IntegerField("Player Class", choices=CLASSES)
    image = models.CharField("Image", max_length=2000, default="")

    def __str__(self):
        return self.name


class CardInDeck(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    numOfCards = models.IntegerField("Number of Cards")


class Team(models.Model):
    name = models.CharField("Name", max_length=200)
    description = models.CharField("Description", max_length=2000, default="")
    img = models.URLField("Image")

    def __str__(self):
        return self.name


class PlayerInTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
