from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Card, Relationship, Metric


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
    slug_first_char = slug[0]
    card_type_exceptions = ['A', 'E']

    # do not include duplicates, continuation cards, and end cards
    if slug_first_char not in card_type_exceptions and slug not in card_history['history']:
        card_history['history'].append(slug)


def reset_card_history():
    card_history['path'] = []
    card_history['history'] = []


def can_publish_status(slug):
    # needs to be an end card
    if slug[0] == 'E':
        status = CARDS.get(card_slug=slug).can_publish_status
    else:
        status = 'n/a'
    return status


def get_question(slug):
    all_cards = CARDS
    question = all_cards.get(card_slug=slug).card_text
    return question


def get_answer(slug, next_slug):
    card = CARDS.get(card_slug=slug)
    rel = RELS.get(card=card.id)
    answer_choice_and_text = []

    if rel.choice_one_next.card_slug == next_slug:
        answer_choice_and_text = ['1', card.choice_one]
    else :
        answer_choice_and_text = ['2', card.choice_two]
    return answer_choice_and_text


def gen_summary():
    summary = []
    path = card_history['path']
    history = card_history['history']
    index = 0

    while index < (len(history) - 1):
        summary.append({
            'slug': history[index],
            'question': get_question(history[index]),
            'answer': get_answer(history[index], history[index + 1])
        })
        index += 1
    # add the last item
    summary.append({
        'slug': history[-1],
        'question': get_question(history[-1]),
        'answer': get_answer(history[-1], path[-1])
    })
    return summary


def set_metrics(summary):
    # Iterate through the summary list.
    # If a slug matches a card_slug in the table,
    # add an increment to the appropriate choice count (one or two).
    # If it does not match an existing slug, create the new record
    # and add the increment to the appropriate choice count.
    record = None

    for item in summary:
        if Metric.objects.filter(card_slug=item['slug']):
            # found a record with the existing slug
            record = Metric.objects.get(card_slug=item['slug'])
        else:
            # need to create a new table row (record)
            record = Metric(card_slug=item['slug'])

        # update the question count
        if item['answer'][0] == '1':
            record.card_choice_one += 1
        else :
            record.card_choice_two += 1

        record.save()
        # reset
        record = None


def set_metrics_grid(metrics_objects):
    metrics_grid = []
    for item in metrics_objects:
        metrics_grid.append({
            'q_slug': item.card_slug,
            'question': get_question(item.card_slug),
            'choice_one': CARDS.get(card_slug=item.card_slug).choice_one,
            'count_one': item.card_choice_one,
            'choice_two': CARDS.get(card_slug=item.card_slug).choice_two,
            'count_two': item.card_choice_two
        })
    return metrics_grid


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
    if card_history['path'][-1] != card_slug and\
        card_history['path'][-1] != rel.choice_back:
        update_card_history(card_slug)

    context = {
        'card': card,
        'rel': rel,
        'card_history': card_history
    }
    return render(request, 'libel/card.html', context)


def summary(request):
    last_card_slug = card_history['history'][-1]
    summary = gen_summary()
    set_metrics(summary)
    context = {
        'last_card': last_card_slug,
        'card_history': card_history,
        'pub_status': can_publish_status(last_card_slug),
        'summary': summary
    }
    return render(request, 'libel/summary.html', context)


def metrics(request):
    all_questions_counted = Metric.objects.order_by('card_slug')
    metrics_grid = set_metrics_grid(all_questions_counted)
    context = { 'metrics_grid': metrics_grid}
    return render(request, 'libel/metrics.html', context)
