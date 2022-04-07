from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /libel/Q1/
    path('<slug:card_slug>/', views.card, name='card'),
    # An ending card can only get accessed via and ending card.
    # The regex is passed as an argument to the view.
    # ex: /libel/E4bA/summary/
    re_path(r'(E[a-zA-Z0-9]*)/summary/', views.summary, name='summary'),
]

