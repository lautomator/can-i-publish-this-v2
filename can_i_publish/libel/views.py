# from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Card, Relationship


def index(request):
    all_cards = Card.objects.all()
    context = {'all_cards': all_cards}

    return render(request, 'libel/index.html', context)


def card(request, card_slug):
    all_cards = Card.objects.all()
    card =  all_cards.get(card_slug=card_slug)
    context = {'card': card}

    return render(request, 'libel/card.html', context)
