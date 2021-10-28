import requests

from django.db import models

# Create your models here.
class Parse(models.Model):
    lokasi = models.CharField(max_length=250)
    sudut = models.CharField(max_length=250)

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        r = requests.get(f"https://arah-kiblat-api.herokuapp.com/{self.lokasi}")
        #r = requests.get(f"http://127.0.0.1:8000/{self.lokasi}")
        self.sudut = r.json()
        super().save(*args, **kwargs)