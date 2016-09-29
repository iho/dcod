from django.db import models

class Region(models.Model):
    name = models.CharField(verbose_name='Region name',max_length=255, unique=True)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(verbose_name='Counrty name', max_length=255, unique=True)
    region = models.ForeignKey(Region, null=True)

    value = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
