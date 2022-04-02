from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is home of Libel with Q1")


def card(request, card_id):
    return HttpResponse("This is a card view.")
