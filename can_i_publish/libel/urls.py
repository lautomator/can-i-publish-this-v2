from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # /libel/summary/
    path('summary/', views.summary, name='summary'),
    path('metrics/', views.metrics, name='metrics'),
    # ex: /libel/Q1/
    path('<slug:card_slug>/', views.card, name='card'),
]

