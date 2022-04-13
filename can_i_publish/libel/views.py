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

    # do not include duplicates, continuation cards, and end cards
    if slug not in card_history['history'] and slug[0] != 'A':
        card_history['history'].append(slug)



def reset_card_history():
    card_history['path'] = []
    card_history['history'] = []


def get_answer(slug, next_slug):
    """
    you can get the answer to the question by looking at
    the previous slug choices (rels). You get that slug from
    the history (the previous slug) and matching it with the
    next slug in the history.
    ex history: [Q1, Q2, E2]
    Q1 choice = if rel.choice Q1 == Q2 then rel.choice = rel.choice 'yes'

    >>> from libel.models import Card, Relationship
    >>> CARDS = Card.objects.all()
    >>> RELS = Relationship.objects.all()
    >>> card = CARDS.get(card_slug='Q1')
    >>> card
    <Card: Q1>
    >>> card.choice_one
    'yes'
    >>> rel = RELS.get(card=card.id)
    >>> rel
    <Relationship: Q1 rel>
    >>> rel.choice_one_next
    <Card: Q2>
    >>> rel.choice_two_next
    <Card: E1>
    rel.choice_two_next.card_slug == 'E1'
    True
    >>> card.choice_two
    'no'

    Therefore, you answered 'no' to Question Q1.
    """

    card = CARDS.get(card_slug=slug)
    rel = RELS.get(card=card.id)
    answer_text = ''

    if rel.choice_one_next.card_slug == next_slug:
        answer_text = card.choice_one
    else :
        answer_text = card.choice_two

    return answer_text


def gen_answer_index():
    answers = {}
    history = card_history['history']
    index = 0

    while index < (len(history) - 1):
        answers[history[index]] = get_answer(history[index], history[index + 1])
        index += 1;

    return answers


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

    context = {
        'card': card,
        'rel': rel,
        'card_history': card_history
    }
    return render(request, 'libel/card.html', context)


def summary(request, last_card_slug):
    context = {
        'last_card': last_card_slug,
        'card_history': card_history,
        'answers': gen_answer_index()
    }
    return render(request, 'libel/summary.html', context)

