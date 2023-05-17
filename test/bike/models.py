from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Extra(models.Model):
    address = models.CharField(max_length=200)
    altitude = models.IntegerField()
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment = models.JSONField()
    payment_terminal = models.BooleanField()
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=200)

class Station(models.Model):
    empty_slots = models.IntegerField()
    extra = models.OneToOneField(Extra, on_delete=models.CASCADE)
    free_bikes = models.IntegerField()
    id_station = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

class Network(models.Model):
    company = models.JSONField()
    gbfs_href = models.URLField()
    href = models.CharField(max_length=200)
    id_network = models.CharField(max_length=200)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    stations = models.ManyToManyField(Station)
    
