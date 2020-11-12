from django.contrib import admin

# Miejsce na rejestracje modeli.

from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)