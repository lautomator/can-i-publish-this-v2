from django.urls import path
from . import views

urlpatterns = [
    # /libel/
    path('', views.index, name='index'),
    # /libel/summary/
    path('summary/', views.summary, name='summary'),
    # /libel/metrics/
    path('metrics/', views.metrics, name='metrics'),
    # ex: /libel/Q1/
    path('<slug:card_slug>/', views.card, name='card'),
]

