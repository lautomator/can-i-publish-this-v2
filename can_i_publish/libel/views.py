from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import Card, Relationship


# These are only updated by the admin.
# They could be part of an API and they
# are easier to maintain in the Admin.
CARDS = Card.objects.all()
RELS = Relationship.objects.all()

card_history = {
    'path': ['Q1'],
    'history': ['Q1'],
}

# ~~~~~~~~~~~~~~~~~~~
# Functions
# ~~~~~~~~~~~~~~~~~~~

def update_card_history(slug):
    card_history['path'].append(slug)

    # do not include duplicates
    if slug not in card_history['history']:
        card_history['history'].append(slug)


def reset_card_history():
    card_history['path'] = []
    card_history['history'] = []


# ~~~~~~~~~~~~~~~~~~~
# Views
# ~~~~~~~~~~~~~~~~~~~

def index(request):
    # index should go to Q1
    return HttpResponseRedirect(reverse('card', args=('Q1',)))


def card(request, card_slug):
    card = CARDS.get(card_slug=card_slug)
    rel = RELS.get(card=card.id)

    # reset if we get to Q1 again
    if card_slug == 'Q1':
        # reset the history
        reset_card_history()
        update_card_history('Q1')

    # avoid duplicate hits if the page is refreshed
    # or if the user goes back to the earlier state.
    if card_history['path'][-1] != card_slug and card_history['path'][-1] != rel.choice_back:
        update_card_history(card_slug)

    context = {'card': card, 'rel': rel, 'card_history': card_history}

    return render(request, 'libel/card.html', context)


def summary(request, last_card_slug):
    context = {
        'last_card': last_card_slug,
        'card_history': card_history,
    }
    return render(request, 'libel/summary.html', context)

