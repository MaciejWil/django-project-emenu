from django.db import models
from django.core.urlresolvers import reverse



# Create your models here.

class Menu(models.Model):
    nazwa = models.CharField(max_length=200,unique=True)
    opis = models.CharField(max_length=1000)
    data_dodania = models.DateField()
    data_aktualizacji = models.DateField()

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse("menu:detail",kwargs={'pk':self.pk})


class Danie(models.Model):
    menu = models.ForeignKey(Menu,related_name='karta')
    nazwa = models.CharField(max_length=200,unique=True)
    opis = models.CharField(max_length=1000)
    cena = models.PositiveIntegerField()
    czas_przygotowania = models.PositiveIntegerField()
    data_dodania = models.DateField()
    data_aktualizacji = models.DateField()
    danie_wegetarianskie = models.BooleanField()
    foto = models.FileField(blank=True)

    def __str__(self):
        return self.nazwa
