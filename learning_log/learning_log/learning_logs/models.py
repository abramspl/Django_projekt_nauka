from django.db import models

# Miejsce na Twoje modele.

class Topic(models.Model):
    """ Temat poznawany przez uzytkownika."""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Zwraca reprezentacje modelu w postaci ciagu tekstowgo."""

        return self.text

class Entry(models.Model):
    """Konkretne informacje o postepie w nauce."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Zwraca reprezentacje modelu w postaci ciagu tekstowego."""

        return f'{self.text[:50]}...'
