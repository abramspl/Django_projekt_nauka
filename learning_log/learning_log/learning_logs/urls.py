"""Definiuje wzorce adresow URL dla learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Strona glowna
    path('', views.index, name='index'),
    # Wyswietlanie wszystkich tematow
    path('topics/', views.topics, name='topics'),
    # Strona szczegolowa dotyczaca pojedynczego tematu.
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),
]