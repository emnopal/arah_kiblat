import requests

from django.db import models

# Create your models here.
class Parse(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    lokasi = models.CharField(max_length=2000)
    sudut = models.CharField(max_length=2000)

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        #r = requests.get(f"https://arah-kiblat-api.herokuapp.com/{self.lokasi}")
        r = requests.get(f"http://127.0.0.1:5500/{self.lokasi}")
        self.sudut = r.json()
        super().save(*args, **kwargs)