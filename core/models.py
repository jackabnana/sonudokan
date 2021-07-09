from django.db import models
from djsingleton.models import SingletonModel


class Ad(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="slots/")
    link = models.URLField(max_length=250)

    def __str__(self):
        return self.title


class AdPlacement(SingletonModel):
    name = models.CharField(max_length=60,help_text="Give a name for this set")
    header1_banners = models.ManyToManyField(
        Ad, related_name="header1", blank=True)
    header2_banners = models.ManyToManyField(
        Ad, related_name="header2", blank=True)

    def __str__(self):
        return "Placed Ad"
