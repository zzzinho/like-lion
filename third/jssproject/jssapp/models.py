from django.db import models

# Create your models here.
class Jasoseol(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
