from django.db import models
from django.urls import reverse

SESSIONS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

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

class Visitor(models.Model):
    date = models.DateField('visiting date')
    session = models.CharField(
        max_length=1,
        choices=SESSIONS,
        default=SESSIONS[0][0]
    )

    lighthouse = models.ForeignKey(Lighthouse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_session_display()} on {self.date}"

    class Meta:
        ordering = ['-date']