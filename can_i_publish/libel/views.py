from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Card, Relationship


def index(request):
    return HttpResponse("This is home of Libel with all of the modules.")


# def card(request, card_id):
#     card = get_object_or_404(Card, pk=card_id)
#     return render(request, 'libel/card')



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
