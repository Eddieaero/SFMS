from django.db import models

# class SensorData(models.Model):
#     id = models.IntegerField(primary_key=True)
#     air_humidity = models.FloatField()  # Percentage
#     air_temperature = models.FloatField(default=0)  # Kelvin
#     soil_temperature = models.FloatField(default=0)  # Kelvin
#     flux = models.IntegerField()  # Percentage
#     rain_drop = models.FloatField()  # Percentage
#     ph = models.FloatField()  # 0-14
#     nitrogen = models.FloatField()  # mg/kg
#     phosphorus = models.FloatField()  # mg/kg
#     potassium = models.FloatField()  # mg/kg
#     timestamp = models.DateTimeField(auto_now_add=True)  # Automatic timestamp


class SensorData(models.Model):
    sensor_data_id = models.AutoField(primary_key=True)
    air_humditity = models.FloatField()
    air_temperature = models.FloatField()
    soil_temperature = models.FloatField()
    flux = models.FloatField(null=True)
    rain_drop = models.FloatField()
    ph_value = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class WeatherData(models.Model):
    rainfall = models.FloatField() # milimeter
    temperature = models.FloatField()  # Kelvin
    humidity = models.FloatField()  # Percentage
    wind_speed = models.FloatField()  # m/s
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatic timestamp