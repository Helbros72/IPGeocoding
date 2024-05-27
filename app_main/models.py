from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)


class History(models.Model):
    ip = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
