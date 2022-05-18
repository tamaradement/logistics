from django.db import models
from django.urls import reverse


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("warehouse_list", args=[str(self.id)])


class Item(models.Model):
    type = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    unit_weight = models.CharField(max_length=200)
    unit_Count = models.CharField(max_length=200)
    location = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("item_detail", args=[str(self.id)])
