from django.db import models

# Create your models here.
class Airline(models.Model):
    name = models.CharField(max_length=40)
    adress = models.CharField(max_length=200)
    description = models.TextField()
    destinations = models.ManyToManyField('Destination', help_text='Select destinations for airline')



class Destination(models.Model):
    city_name = models.CharField(max_length=120)
    airport_name = models.CharField(max_length=120)
