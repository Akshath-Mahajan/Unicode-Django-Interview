from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.TextField()
    country = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    weather = models.TextField()
    description = models.TextField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    visibility = models.FloatField()
    wind_speed = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.city+":"+str(self.date)