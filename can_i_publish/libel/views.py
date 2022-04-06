# from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Card, Relationship

# These are static
CARDS = Card.objects.all()
RELS = Relationship.objects.all()

def index(request):
    all_cards = CARDS.order_by("card_type")
    context = {'all_cards': all_cards}

    return render(request, 'libel/index.html', context)


def card(request, card_slug):
    card = CARDS.get(card_slug=card_slug)
    context = {'card': card}

    return render(request, 'libel/card.html', context)
