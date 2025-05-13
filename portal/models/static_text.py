from django.db import models

class StaticText(models.Model):
    key = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.key
