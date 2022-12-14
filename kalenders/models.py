from django.db import models


class Kalender(models.Model):
    jaar = models.PositiveSmallIntegerField(unique=True)
    opmerkingen = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Kalender {self.jaar}"
