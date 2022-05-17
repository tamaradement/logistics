from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    unit_weight = models.CharField(max_length=200)
    unit_Count = models.CharField(max_length=200)

    def __str__(self):
        return self.type
