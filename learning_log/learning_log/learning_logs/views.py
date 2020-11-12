from django.shortcuts import render

# Miejsce na utworzenie widokow
def index(request):
    """Strona glowna dla aplikacji Learning Log"""

    return render(request, 'learning_logs/index.html')
