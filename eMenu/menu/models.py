from django.db import models
from django.core.urlresolvers import reverse



# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=1000)
    added_date = models.DateField()
    update_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("menu:detail",kwargs={'pk':self.pk})


class Dish(models.Model):
    menu = models.ForeignKey(Menu,related_name='emenu')
    name = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=1000)
    price = models.PositiveIntegerField()
    preparation_time = models.PositiveIntegerField()
    added_date = models.DateField()
    update_date = models.DateField(blank=True,null=True)
    vegetarian = models.BooleanField()
    foto = models.FileField(blank=True)

    def __str__(self):
        return self.name
