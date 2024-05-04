from django.db import models
import jsonfield    

class SensorData(models.Model):
    sensor_data_id = models.AutoField(primary_key=True)
    air_humidity = models.FloatField(default=0.0)
    air_temperature = models.FloatField()
    soil_temperature = models.FloatField()
    flux = models.FloatField(null=True)
    rain_drop = models.FloatField()
    ph_value = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    recommendations = jsonfield.JSONField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class WeatherData(models.Model):
    rainfall = models.FloatField() # milimeter
    temperature = models.FloatField()  # Kelvin
    humidity = models.FloatField()  # Percentage
    wind_speed = models.FloatField()  # m/s
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatic timestamp