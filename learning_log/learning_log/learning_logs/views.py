from django.shortcuts import render
from .models import Topic

# Miejsce na utworzenie widokow
def index(request):
    """Strona glowna dla aplikacji Learning Log"""

    return render(request, 'learning_logs/index.html')

def topics(request):
    """Wyswietlenie wszystkich tematow."""

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Wyswietla pojedynczy temat i wszystkie powiazane z nim wpisy."""

    topic =Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)