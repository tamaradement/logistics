from django.db import models
from django.urls import reverse


class Item(models.Model):
    type = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    unit_weight = models.CharField(max_length=200)
    unit_Count = models.CharField(max_length=200)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("item_detail", args=[str(self.id)])
