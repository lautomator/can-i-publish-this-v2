# from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Card, Relationship

# These are static
CARDS = Card.objects.all()
RELS = Relationship.objects.all()

def index(request):
    card = CARDS.get(card_slug='Q1')
    rel = RELS.get(card=card.id)
    context = {'card': card, 'rel': rel}

    return render(request, 'libel/index.html', context)


def card(request, card_slug):
    card = CARDS.get(card_slug=card_slug)
    rel = RELS.get(card=card.id)
    context = {'card': card, 'rel': rel}

    return render(request, 'libel/card.html', context)


def summary(request, last_card_slug):
    return render(request, 'libel/summary.html', {'last_card': last_card_slug})