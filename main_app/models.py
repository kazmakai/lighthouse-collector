from django.db import models
from django.urls import reverse

class Lighthouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    height = models.IntegerField()
    built = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'lighthouse_id': self.id})