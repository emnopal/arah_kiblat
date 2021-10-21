import requests

from django.db import models

# Create your models here.
class Parse(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    lokasi = models.CharField(max_length=1000)
    sudut = models.CharField(max_length=1000)

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        r = requests.get(f"https://arah-kiblat-api.herokuapp.com/{self.lokasi}")
        self.sudut = r.json()
        super().save(*args, **kwargs)