"""Definiuje wzorce adresow URL dla learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Strona glowna
    path('', views.index, name='index'),
]