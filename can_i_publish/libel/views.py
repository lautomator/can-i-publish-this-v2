from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Card, Relationship


def index(request):
    return HttpResponse("This is home of the Libel module. This should have question 1.")


def card(request, card_slug):
    card = Card.objects.get(pk=card_slug)
    card_text = card.card_text
    return HttpResponse(card_text)



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
