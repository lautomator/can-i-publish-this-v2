from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /libel/Q1/
    path('<card_slug>/', views.card, name='card'),
]

